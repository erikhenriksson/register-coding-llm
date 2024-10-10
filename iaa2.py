import json
import os
import numpy as np
from sklearn.metrics import cohen_kappa_score
from scipy.stats import pearsonr


def load_jsonl(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def compute_iaa(true_labels, llm_labels, threshold=4):
    # Identify all possible label categories
    all_labels = set(label for labels in true_labels for label in labels)
    all_labels.update(label for labels in llm_labels for label in labels.keys())
    all_labels = list(all_labels)

    kappas = []
    pearsons = []

    for label in all_labels:
        true_label_values = []
        llm_label_values = []

        for true, llm in zip(true_labels, llm_labels):
            # Convert true label presence to match the threshold scale
            true_label_values.append(threshold if label in true else 0)
            # Use the continuous score directly for the LLM, but cap it at the threshold
            llm_score = min(llm.get(label, 0), threshold)
            llm_label_values.append(llm_score)

        # Compute weighted kappa and Pearson correlation
        kappas.append(
            cohen_kappa_score(true_label_values, llm_label_values, weights="quadratic")
        )
        pearsons.append(pearsonr(true_label_values, llm_label_values)[0])

    # Overall agreement scores
    avg_kappa = np.nanmean(kappas)
    avg_pearson = np.nanmean(pearsons)

    return avg_kappa, avg_pearson


def process_language_data(language_dir, threshold=6):
    file_path = os.path.join(language_dir, "train.jsonl")
    data = load_jsonl(file_path)

    # Extract labels
    true_labels = [item["label"] for item in data]
    llm_labels = [item["llm_label"] for item in data]

    # Compute IAA
    avg_kappa, avg_pearson = compute_iaa(true_labels, llm_labels, threshold)

    return avg_kappa, avg_pearson


def main():
    languages = ["en", "fi", "fr"]  # specify the languages to process
    overall_kappas = []
    overall_pearsons = []

    for lang in languages:
        lang_dir = f"{lang}"
        avg_kappa, avg_pearson = process_language_data(lang_dir)
        overall_kappas.append(avg_kappa)
        overall_pearsons.append(avg_pearson)
        print(
            f"Language: {lang} | Weighted Cohen's Kappa: {avg_kappa:.4f} | Pearson's r: {avg_pearson:.4f}"
        )

    # Overall scores across all languages
    total_avg_kappa = np.mean(overall_kappas)
    total_avg_pearson = np.mean(overall_pearsons)
    print(
        f"Overall | Weighted Cohen's Kappa: {total_avg_kappa:.4f} | Pearson's r: {total_avg_pearson:.4f}"
    )


# Run the main function
main()
