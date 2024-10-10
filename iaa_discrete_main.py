import json
import os
from scipy.stats import pearsonr
from sklearn.metrics import cohen_kappa_score
import numpy as np
import glob


# Define function to load data
def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


# Define the parent category mappings
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

# List of parent categories
parent_categories = list(labels_structure.keys())


# Function to map label to parent categories
def map_to_parent_categories(label):
    # Check direct mappings from label_structure
    for parent, children in labels_structure.items():
        if label in children:
            return parent
    # Check other_labels
    for parent, other_label in other_labels.items():
        if label == other_label:
            return parent
    return None  # Return None if label doesn't map to any parent


# Convert original labels to parent categories
def labels_to_parent_vector(true_labels, llm_labels):
    # Initialize vectors
    true_vector = np.zeros(len(parent_categories), dtype=int)
    llm_vector = np.zeros(len(parent_categories), dtype=int)

    # Convert human labels
    for label in true_labels:
        parent = map_to_parent_categories(label)
        if parent:
            parent_index = parent_categories.index(parent)
            true_vector[parent_index] = 1

    # Convert LLM labels
    for label, value in llm_labels.items():
        parent = map_to_parent_categories(label)
        if parent and value == 1:
            parent_index = parent_categories.index(parent)
            llm_vector[parent_index] = 1

    return true_vector, llm_vector


# Calculate Cohen's Kappa and Pearson's r for each language dataset
def calculate_iaa(data):
    kappa_scores = []
    pearson_r_scores = []

    for entry in data:
        true_labels = entry["label"]
        llm_labels = entry["llm_label"]

        # Convert labels to parent category binary vectors
        true_vector, llm_vector = labels_to_parent_vector(true_labels, llm_labels)

        # Calculate Cohen's Kappa for each entry
        kappa_score = cohen_kappa_score(true_vector, llm_vector)
        kappa_scores.append(kappa_score)

        # Calculate Pearson's r for each entry
        pearson_r, _ = pearsonr(true_vector, llm_vector)
        pearson_r_scores.append(pearson_r)

    # Average Kappa and Pearson's r
    avg_kappa = np.nanmean(kappa_scores)
    avg_pearson_r = np.nanmean(pearson_r_scores)

    return avg_kappa, avg_pearson_r


# Process files for each language
languages = ["en", "fi", "fr", "sv", "tr"]
results = {}

for lang in languages:
    filepath = f"{lang}/train_discrete.jsonl"
    data = load_data(filepath)
    kappa, pearson_r = calculate_iaa(data)
    results[lang] = {"Cohen's Kappa": kappa, "Pearson's r": pearson_r}
    print(f"{lang} - Cohen's Kappa: {kappa}, Pearson's r: {pearson_r}")

# Aggregate all languages
all_data = []
for lang in languages:
    filepath = f"{lang}/train_discrete.jsonl"
    all_data.extend(load_data(filepath))

overall_kappa, overall_pearson_r = calculate_iaa(all_data)
results["overall"] = {"Cohen's Kappa": overall_kappa, "Pearson's r": overall_pearson_r}


print(
    f"Overall - Cohen's Kappa: {overall_kappa:.2f}, Pearson's r: {overall_pearson_r:.2f}"
)


# Print final results
print("Final Results:")
for lang, metrics in results.items():
    print(f"{lang}: {metrics}")
