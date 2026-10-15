"""Module 09: Final findings generated from the real Daraz datasource."""

import pandas as pd


def generate_findings(raw_csv_path, cleaned_csv_path):
    """Compute final project findings from the actual raw and cleaned files."""
    raw_df = pd.read_csv(raw_csv_path)
    df = pd.read_csv(cleaned_csv_path)

    category_price = df.groupby("Category")["Current Price"].median().sort_values(ascending=False)
    category_sales = df.groupby("Category")["Sold Count"].median().sort_values(ascending=False)

    correlations = df[[
        "Current Price", "Rating in Stars", "Rating Count", "Discount %", "Sold Count"
    ]].corr()["Sold Count"].drop("Sold Count")

    findings = {
        "raw_rows": int(len(raw_df)),
        "unique_product_rows": int(len(df)),
        "median_price": float(df["Current Price"].median()),
        "mean_price": float(df["Current Price"].mean()),
        "highest_median_price_category": category_price.index[0],
        "highest_median_price": float(category_price.iloc[0]),
        "highest_median_sold_category": category_sales.index[0],
        "highest_median_sold": float(category_sales.iloc[0]),
        "lowest_median_sold_category": category_sales.index[-1],
        "lowest_median_sold": float(category_sales.iloc[-1]),
        "price_sold_correlation": float(correlations["Current Price"]),
        "rating_sold_correlation": float(correlations["Rating in Stars"]),
        "rating_count_sold_correlation": float(correlations["Rating Count"]),
        "discount_sold_correlation": float(correlations["Discount %"]),
    }

    limitations = [
        "The dataset is a snapshot rather than a time series, so it cannot show changes over time.",
        "Sold Count is a marketplace-reported field and some values are rounded, for example 6K Sold.",
        "Correlation describes association, not causation.",
        "The dataset contains selected product categories, so conclusions should not be generalized to all Daraz products.",
        "Price groups are analyst-defined thresholds used for this project, not official Daraz categories.",
    ]

    return findings, limitations
