"""Module 06: Pandas analysis using the cleaned real Daraz datasource."""

import pandas as pd
from module03_conditions import price_group


def run_pandas_analysis(cleaned_csv_path, analysis_output_path="daraz_analysis_ready.csv"):
    """Answer the main project questions with pandas on real cleaned data."""
    df = pd.read_csv(cleaned_csv_path)

    # Apply a real classification rule to every cleaned product price.
    groups = []
    for price in df["Current Price"]:
        groups.append(price_group(price))
    df["Price Group"] = groups

    category_counts = df["Category"].value_counts()
    category_summary = df.groupby("Category").agg(
        products=("Title", "count"),
        median_price=("Current Price", "median"),
        median_sold=("Sold Count", "median"),
        average_rating=("Rating in Stars", "mean"),
        median_rating_count=("Rating Count", "median"),
        median_discount_pct=("Discount %", "median"),
    ).round(2)

    delivery_summary = df.groupby("Delivery")[["Current Price", "Sold Count", "Rating in Stars"]].median()
    voucher_summary = df.groupby("Has Voucher")[["Current Price", "Sold Count", "Rating in Stars"]].median()
    price_group_summary = df.groupby("Price Group")[["Sold Count", "Rating in Stars"]].median()

    top_sold = df.nlargest(5, "Sold Count")[[
        "Title", "Category", "Sold Count", "Current Price", "Rating in Stars", "Rating Count"
    ]]

    overall = {
        "cheapest_price": float(df["Current Price"].min()),
        "most_expensive_price": float(df["Current Price"].max()),
        "mean_price": float(df["Current Price"].mean()),
        "median_price": float(df["Current Price"].median()),
        "available_sold_count_sum": int(df["Sold Count"].sum()),
        "products_with_no_customer_rating": int((df["Rating Count"] == 0).sum()),
    }

    df.to_csv(analysis_output_path, index=False)

    return {
        "data": df,
        "category_counts": category_counts,
        "category_summary": category_summary,
        "delivery_summary": delivery_summary,
        "voucher_summary": voucher_summary,
        "price_group_summary": price_group_summary,
        "top_sold": top_sold,
        "overall": overall,
        "analysis_output_path": analysis_output_path,
    }
