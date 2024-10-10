import json
import os
import numpy as np
from sklearn.metrics import cohen_kappa_score
from scipy.stats import pearsonr
import warnings

# Define initial threshold
INITIAL_THRESHOLD = 5

# Define the possible labels in the dataset (based on hierarchy)
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

# Define languages
# languages = ["en", "fi", "fr", "sv", "tr"]
languages = ["en", "fi", "fr"]

# Store kappa and Pearson results
language_results = {}


# Function to get binary vectors from labels
def get_binary_vector(label_list, label_space):
    return [1 if label in label_list else 0 for label in label_space]


# Function to apply thresholding with fallback mechanism
def apply_threshold_with_fallback(label_dict, labels, initial_threshold):
    thresholded_vector = [
        1 if label_dict.get(label, 0) >= initial_threshold else 0 for label in labels
    ]

    # Lower threshold until we have at least one label
    current_threshold = initial_threshold
    while sum(thresholded_vector) == 0:
        current_threshold -= 1
        thresholded_vector = [
            1 if label_dict.get(label, 0) >= current_threshold else 0
            for label in labels
        ]

    return thresholded_vector


# Process each language
for lang in languages:
    file_path = f"{lang}/train_discrete.jsonl"

    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        continue

    # Load data
    manual_labels = []
    llm_labels = []

    with open(file_path, "r") as f:
        for line in f:
            data = json.loads(line)
            # Convert manual labels to a binary vector
            manual_label_vector = get_binary_vector(data["label"], all_labels)
            manual_labels.append(manual_label_vector)

            # Apply threshold with fallback for LLM labels
            thresholded_llm_labels = apply_threshold_with_fallback(
                data["llm_label"], all_labels, INITIAL_THRESHOLD
            )
            llm_labels.append(thresholded_llm_labels)

    # Convert lists to numpy arrays
    manual_labels = np.array(manual_labels)
    llm_labels = np.array(llm_labels)

    # Calculate Cohen's Kappa for each label independently and take average
    kappas = []
    pearsons = []
    for i in range(len(all_labels)):
        # Suppress warnings for constant input
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning)
            warnings.filterwarnings("ignore", category=RuntimeWarning)

            # Cohen's Kappa
            kappa = cohen_kappa_score(manual_labels[:, i], llm_labels[:, i])
            if not np.isnan(kappa):
                kappas.append(kappa)

            # Pearson's R
            # Only calculate Pearson's if the input isn't constant
            if len(set(manual_labels[:, i])) > 1 and len(set(llm_labels[:, i])) > 1:
                pearson = pearsonr(manual_labels[:, i], llm_labels[:, i])[0]
                if not np.isnan(pearson):
                    pearsons.append(pearson)

    # Average kappa and pearson across all labels (excluding NaNs)
    avg_kappa = np.mean(kappas) if kappas else float("nan")
    avg_pearson = np.mean(pearsons) if pearsons else float("nan")

    # Store results
    language_results[lang] = {
        "average_kappa": avg_kappa,
        "average_pearson": avg_pearson,
    }

    print(
        f"{lang} - Average Cohen's Kappa: {avg_kappa}, Average Pearson's R: {avg_pearson}"
    )

# Overall Metrics
# Stack all manual and LLM labels for overall kappa and pearson calculations
combined_manual_labels = np.vstack([manual_labels for manual_labels in manual_labels])
combined_llm_labels = np.vstack([llm_labels for llm_labels in llm_labels])

overall_kappas = []
overall_pearsons = []

for i in range(len(all_labels)):
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        warnings.filterwarnings("ignore", category=RuntimeWarning)

        kappa = cohen_kappa_score(
            combined_manual_labels[:, i], combined_llm_labels[:, i]
        )
        if not np.isnan(kappa):
            overall_kappas.append(kappa)

        if (
            len(set(combined_manual_labels[:, i])) > 1
            and len(set(combined_llm_labels[:, i])) > 1
        ):
            pearson = pearsonr(combined_manual_labels[:, i], combined_llm_labels[:, i])[
                0
            ]
            if not np.isnan(pearson):
                overall_pearsons.append(pearson)

# Average kappa and pearson across all labels (excluding NaNs)
overall_avg_kappa = np.mean(overall_kappas) if overall_kappas else float("nan")
overall_avg_pearson = np.mean(overall_pearsons) if overall_pearsons else float("nan")

print(
    f"Overall - Average Cohen's Kappa: {overall_avg_kappa}, Average Pearson's R: {overall_avg_pearson}"
)
