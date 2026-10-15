"""Module 02: Loops applied to the real Daraz datasource only."""

import pandas as pd


def category_counts_with_loop(csv_path):
    """Count actual Daraz categories using a for loop instead of value_counts()."""
    df = pd.read_csv(csv_path)
    counts = {}

    for category in df["Category"].dropna():
        if category in counts:
            counts[category] += 1
        else:
            counts[category] = 1

    return dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))


def missing_values_with_loop(csv_path):
    """Count missing values column-by-column using a loop on the real data."""
    df = pd.read_csv(csv_path)
    missing = {}

    for column in df.columns:
        missing[column] = int(df[column].isna().sum())

    return missing
