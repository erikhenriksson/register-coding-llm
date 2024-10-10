import json
import os

os.environ["HF_HOME"] = ".hf/hf_home"

import re
import gzip
import csv
import sys
import torch
from transformers import pipeline

# Increase the field size limit
csv.field_size_limit(sys.maxsize)

from openai import OpenAI
import prompt_core_complex_discrete as prompt_core

# Define the languages to process
languages = ["en", "fi", "fr", "sv", "tr"]
model_id = "gpt-4o-mini"

# get model from sys argv 1
if len(sys.argv) > 1:
    model_id = sys.argv[1]

if "llama" in model_id:
    from huggingface_hub import login

    login(token=os.getenv("HF_API_KEY", ""))

    llama_pipeline = pipeline(model=model_id, device="cuda", torch_dtype=torch.bfloat16)

elif "gpt" in model_id:
    # Define the access token for OpenAI
    access_token = os.getenv("OPENAI_ACCESS_TOKEN", "")
    client = OpenAI()

labels_structure = {
    "MT": [],
    "LY": [],
    "SP": ["it"],
    "ID": [],
    "NA": ["ne", "sr", "nb"],
    "HI": ["re"],
    "IN": ["en", "ra", "dtp", "fi", "lt"],
    "OP": ["rv", "ob", "rs", "av"],
    "IP": ["ds", "ed"],
}

other_labels = {
    "SP": "os",
    "NA": "on",
    "HI": "oh",
    "IN": "oi",
    "OP": "oo",
    "IP": "oe",
}


def format_labels(doc_labels):
    doc_labels = doc_labels.split()
    updated_labels = [
        (
            other_labels.get(label, label)
            if label in labels_structure.keys()
            and not set(labels_structure[label]).intersection(doc_labels)
            else label
        )
        for label in doc_labels
    ]

    labels_with_children = [
        label for label in labels_structure.keys() if labels_structure[label]
    ]

    return sorted(
        [label for label in updated_labels if label not in labels_with_children]
    )


def parse_response(text):
    output_dict = {}
    lines = text.splitlines()

    main_label_pattern = re.compile(r"([A-Z]{2})\s*\(.*?\):\s*(\d+)")
    sub_label_pattern = re.compile(r"-\s*([a-z]{2,3})\s*\(.*?\):\s*(\d+)")

    for line in lines:
        line = line.strip()

        main_match = main_label_pattern.match(line)
        if main_match:
            key, value = main_match.groups()
            output_dict[key] = int(value)
            continue

        sub_match = sub_label_pattern.match(line)
        if sub_match:
            key, value = sub_match.groups()
            output_dict[key] = int(value)

    print(output_dict)
    return output_dict


def get_openai_response(content_instruct, model_id="gpt-4o-mini"):
    completion = client.chat.completions.create(
        model=model_id,
        messages=[
            {"role": "user", "content": content_instruct},
        ],
        temperature=0.0,
    )

    model_output = completion.choices[0].message.content

    return model_output


def get_llama_response(content_instruct, model_id="meta-llama/Llama-3.2-3B-Instruct"):
    messages = [
        {"role": "user", "content": content_instruct},
    ]
    generator = llama_pipeline(
        model=model_id, device="cuda", torch_dtype=torch.bfloat16
    )
    generation = generator(
        messages, do_sample=True, temperature=0.01, max_new_tokens=1000
    )
    model_output = generation[0]["generated_text"][-1]["content"]

    return model_output


def get_response(content, model_id="gpt-4o-mini"):
    content_instruct = prompt_core.MESSAGE.format(content)
    if "gpt" in model_id:
        model_output = get_openai_response(content_instruct, model_id)
    else:
        model_output = get_llama_response(content_instruct, model_id)

    try:
        response = parse_response(model_output)
    except Exception as e:
        print(f"Error: {e}, using model {model_id}")
        print(model_output)
        response = None

    return response


# Iterate over each language
for lang in languages:
    file_path = f"../multilingual-CORE/{lang}/train.tsv.gz"
    output_path = f"{lang}/train_{model_id.replace('/', '_')}.jsonl"
    limit = 100
    processed = 0

    # Ensure output directory exists
    os.makedirs(lang, exist_ok=True)

    # Check if the output file exists and count the number of labeled lines
    if os.path.exists(output_path):
        with open(output_path, "r", encoding="utf-8") as f_out:
            labeled_lines = sum(1 for _ in f_out)
    else:
        labeled_lines = 0

    # Open the gzipped file and skip the already labeled lines
    with gzip.open(file_path, mode="rt", encoding="utf-8") as f_in:
        # Use csv.reader to parse TSV data
        tsv_reader = csv.reader(f_in, delimiter="\t")

        # Skip lines that have already been processed
        for _ in range(labeled_lines):
            next(tsv_reader, None)

        # check if file exists, if not create it
        if not os.path.exists(output_path):
            with open(output_path, "w", encoding="utf-8") as f_out:
                pass

        # Process each row
        for row in tsv_reader:
            if processed >= limit:
                break
            label = row[0]
            text = row[1][:5000]  # Trim text to 5000 characters

            # Generate LLM label from the text
            llm_label = get_response(text, model_id)

            # Create dictionary for output row
            output_row = {
                "label": format_labels(label),
                "llm_label": llm_label,
                "text": text,
            }

            # Open file in append mode and write the output row to the JSONL file
            with open(output_path, "a", encoding="utf-8") as f_out:
                json.dump(output_row, f_out, ensure_ascii=False)
                f_out.write("\n")

            processed += 1

    print(f"Processed and saved data for language: {lang}")
