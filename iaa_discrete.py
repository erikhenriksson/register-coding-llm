import json
import os
from scipy.stats import pearsonr
from sklearn.metrics import cohen_kappa_score
import numpy as np
import glob

# Define the parent category mappings
labels_structure = {
    "MT": ["MT"],
    "LY": ["LY"],
    "SP": ["SP", "it"],
    "ID": ["ID"],
    "NA": ["NA", "ne", "sr", "nb"],
    "HI": ["RE", "re"],
    "IN": ["IN", "en", "ra", "dtp", "fi", "lt"],
    "OP": ["OP", "rv", "ob", "rs", "av"],
    "IP": ["IP", "ds", "ed"],
}

other_labels = {
    "SP": "os",
    "NA": "on",
    "HI": "oh",
    "IN": "oi",
    "OP": "oo",
    "IP": "oe",
}

# All individual labels
all_labels = [
    "MT",
    "LY",
    "it",
    "os",
    "ID",
    "ne",
    "sr",
    "nb",
    "on",
    "re",
    "oh",
    "en",
    "ra",
    "dtp",
    "fi",
    "lt",
    "oi",
    "rv",
    "ob",
    "rs",
    "av",
    "oo",
    "ds",
    "ed",
    "oe",
]

# List of parent categories
parent_categories = list(labels_structure.keys())


# Define function to load data
def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [json.loads(line) for i, line in enumerate(f)]


# Convert labels to binary vector based on all possible labels
def labels_to_vector(true_labels, llm_labels):
    true_vector = np.array([1 if label in true_labels else 0 for label in all_labels])
    llm_vector = np.array([llm_labels.get(label, 0) for label in all_labels])
    return true_vector, llm_vector


# Convert labels to binary vector based on parent categories
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


# Map individual labels to parent categories
def map_to_parent_categories(label):
    # Check direct mappings from label_structure
    for parent, children in labels_structure.items():
        if label in children:
            return parent
    # Check other_labels
    for parent, other_label in other_labels.items():
        if label == other_label:
            return parent

    print(f"Label {label} not found in parent categories")
    exit()
    return None  # Return None if label doesn't map to any parent


from sklearn.metrics import cohen_kappa_score, f1_score
import numpy as np
from scipy.stats import pearsonr

# Calculate Cohen's Kappa, Pearson's r, and F1-score for each language dataset
def calculate_iaa(data, label_scheme="individual"):
    kappa_scores = []
    pearson_r_scores = []
    
    if label_scheme == "individual":
        labels = all_labels
        label_vectors = [labels_to_vector(entry["label"], entry["llm_label"]) for entry in data]
    elif label_scheme == "parent":
        labels = parent_categories
        label_vectors = [labels_to_parent_vector(entry["label"], entry["llm_label"]) for entry in data]
    else:
        raise ValueError("label_scheme must be either 'individual' or 'parent'")
    
    true_vectors = np.array([tv for tv, _ in label_vectors])
    llm_vectors = np.array([lv for _, lv in label_vectors])
    
    # Overall Kappa and Pearson's r for each instance
    for i in range(len(data)):
        if np.all(true_vectors[i] == 0) and np.all(llm_vectors[i] == 0):
            # If both vectors are all zeros, skip Kappa and assign NaN
            kappa_score = np.nan
        else:
            # Calculate Cohen's Kappa normally
            kappa_score = cohen_kappa_score(true_vectors[i], llm_vectors[i], labels=[0, 1])
        
        kappa_scores.append(kappa_score)
        
        # Pearson's r for the instance
        if np.any(true_vectors[i]) or np.any(llm_vectors[i]):  # Only if there is at least one non-zero
            pearson_r, _ = pearsonr(true_vectors[i], llm_vectors[i])
        else:
            pearson_r = np.nan
        pearson_r_scores.append(pearson_r)

    avg_kappa = np.nanmean(kappa_scores)
    avg_pearson_r = np.nanmean(pearson_r_scores)
    
    # Per-label Kappa calculation across all instances
    label_kappa_scores = {}
    for idx, label in enumerate(labels):
        if np.all(true_vectors[:, idx] == 0) and np.all(llm_vectors[:, idx] == 0):
            # Skip labels with no variability
            label_kappa_scores[label] = np.nan
        else:
            label_kappa = cohen_kappa_score(true_vectors[:, idx], llm_vectors[:, idx], labels=[0, 1])
            label_kappa_scores[label] = round(label_kappa, 2)

    # Calculate micro-averaged F1-score
    f1_micro = f1_score(true_vectors, llm_vectors, average="micro")

    return avg_kappa, avg_pearson_r, label_kappa_scores, f1_micro


# Process files for each language
languages = ["en", "fi", "fr", "sv", "tr"]
results_individual = {}
results_parent = {}

for lang in languages:
    filepath = f"{lang}/train_discrete.jsonl"
    data = load_data(filepath)
    
    # Calculate IAA for individual labels
    kappa_individual, pearson_r_individual, label_kappas_individual, f1_individual = calculate_iaa(data, label_scheme="individual")
    results_individual[lang] = {
        "Cohen's Kappa": round(kappa_individual, 2),
        "Pearson's r": round(pearson_r_individual, 2),
        "Label-wise Kappa": label_kappas_individual,
        "F1 Micro": round(f1_individual, 2)
    }
    
    # Calculate IAA for parent labels
    kappa_parent, pearson_r_parent, label_kappas_parent, f1_parent = calculate_iaa(data, label_scheme="parent")
    results_parent[lang] = {
        "Cohen's Kappa": round(kappa_parent, 2),
        "Pearson's r": round(pearson_r_parent, 2),
        "Label-wise Kappa": label_kappas_parent,
        "F1 Micro": round(f1_parent, 2)
    }

# Aggregate all languages
all_data = []
for lang in languages:
    filepath = f"{lang}/train_discrete.jsonl"
    all_data.extend(load_data(filepath))

# Overall for individual labels
overall_kappa_individual, overall_pearson_r_individual, overall_label_kappas_individual, overall_f1_individual = calculate_iaa(all_data, label_scheme="individual")
results_individual["overall"] = {
    "Cohen's Kappa": round(overall_kappa_individual, 2),
    "Pearson's r": round(overall_pearson_r_individual, 2),
    "Label-wise Kappa": overall_label_kappas_individual,
    "F1 Micro": round(overall_f1_individual, 2)
}

# Overall for parent labels
overall_kappa_parent, overall_pearson_r_parent, overall_label_kappas_parent, overall_f1_parent = calculate_iaa(all_data, label_scheme="parent")
results_parent["overall"] = {
    "Cohen's Kappa": round(overall_kappa_parent, 2),
    "Pearson's r": round(overall_pearson_r_parent, 2),
    "Label-wise Kappa": overall_label_kappas_parent,
    "F1 Micro": round(overall_f1_parent, 2)
}

# Print final results
print("Results:")
print("Full scheme (25 labels):")
for lang, metrics in results_individual.items():
    print(f"{lang} - Kappa: {metrics['Cohen\'s Kappa']}, Pearson\'s r: {metrics['Pearson\'s r']}, F1 Micro: {metrics['F1 Micro']}")
    if lang == "overall":
        print("Label-wise Kappa:")
        for label, kappa in metrics["Label-wise Kappa"].items():
            print(f"  {label}: {kappa}")

print("\nParent labels only:")
for lang, metrics in results_parent.items():
    print(f"{lang} - Kappa: {metrics['Cohen\'s Kappa']}, Pearson\'s r: {metrics['Pearson\'s r']}, F1 Micro: {metrics['F1 Micro']}")
    
    if lang == "overall":
        print("Label-wise Kappa:")
        for label, kappa in metrics["Label-wise Kappa"].items():
            print(f"  {label}: {kappa}")
