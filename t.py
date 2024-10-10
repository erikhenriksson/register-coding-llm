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


print(format_labels("OP rv"))  # Should return "rv"
print(format_labels("OP"))  # Should return "oo"
print(format_labels("NA ne"))  # Should return "ne"
print(format_labels("IN"))  # Should return "oi"
print(format_labels("LY OP"))  # Should return "LY oo"
print(
    format_labels("rv OP LY ID NA ne sr")
)  # Should handle multiple and return correctly
