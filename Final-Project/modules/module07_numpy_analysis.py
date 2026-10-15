"""Module 07: NumPy statistics and relationship analysis on real Daraz data."""

import pandas as pd
import numpy as np


def run_numpy_analysis(cleaned_csv_path):
    """Use NumPy arrays, percentiles, IQR, boolean comparisons and correlation."""
    df = pd.read_csv(cleaned_csv_path)

    sold_array = df["Sold Count"].dropna().to_numpy(dtype=float)
    q1, median, q3 = np.percentile(sold_array, [25, 50, 75])
    iqr = q3 - q1
    upper_iqr_threshold = q3 + 1.5 * iqr
    above_threshold = int(np.sum(sold_array > upper_iqr_threshold))

    rating_sales = df[["Rating Count", "Sold Count"]].dropna()
    rating_count_array = rating_sales["Rating Count"].to_numpy(dtype=float)
    sold_count_array = rating_sales["Sold Count"].to_numpy(dtype=float)
    rating_sales_corr = float(np.corrcoef(rating_count_array, sold_count_array)[0, 1])

    # Keep the wider relationship table for interpretation.
    relationship_corr = df[[
        "Current Price", "Rating in Stars", "Rating Count", "Discount %", "Sold Count"
    ]].corr()["Sold Count"].drop("Sold Count").sort_values(ascending=False)

    return {
        "available_sold_records": int(sold_array.size),
        "q1": float(q1),
        "median": float(median),
        "q3": float(q3),
        "iqr": float(iqr),
        "upper_iqr_threshold": float(upper_iqr_threshold),
        "records_above_threshold": above_threshold,
        "numpy_rating_count_vs_sold_corr": rating_sales_corr,
        "relationship_correlations": relationship_corr,
    }
