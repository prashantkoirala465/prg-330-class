"""Module 05: Data cleaning pipeline for the real Daraz datasource."""

import pandas as pd
from module03_conditions import delivery_label, voucher_label
from module04_functions import (
    clean_current_price,
    clean_original_price,
    clean_rating,
    sold_to_number,
    calculate_discount,
)


def clean_dataset(csv_path, output_path="daraz_cleaned_data.csv"):
    """Clean the actual Daraz CSV and save a reusable cleaned datasource."""
    df = pd.read_csv(csv_path)
    raw_rows = len(df)
    exact_duplicates = int(df.duplicated().sum())
    repeated_links = int(df.duplicated(subset=["Link"]).sum())

    # Link is the best product identifier in this datasource.
    df = df.drop_duplicates(subset=["Link"], keep="first").copy()

    # Use reusable functions on real datasource columns.
    df["Current Price"] = df["Current Price"].apply(clean_current_price)
    df["Original Price"] = df["Original Price"].apply(clean_original_price)
    df["Rating in Stars"] = [
        clean_rating(value, count)
        for value, count in zip(df["Rating in Stars"], df["Rating Count"])
    ]

    sold_numbers = []
    for value in df["Sold Count"]:
        sold_numbers.append(sold_to_number(value))
    df["Sold Count"] = sold_numbers

    df["Delivery"] = df["Delivery"].apply(delivery_label)
    df["Has Voucher"] = df["Voucher"].apply(voucher_label)

    discounts = []
    discount_percents = []
    for original, current in zip(df["Original Price"], df["Current Price"]):
        amount, percent = calculate_discount(original, current)
        discounts.append(amount)
        discount_percents.append(percent)
    df["Discount"] = discounts
    df["Discount %"] = discount_percents

    # Drop fields not needed after identification and cleaning.
    df = df.drop(columns=["Voucher", "Currency", "Link"])

    df.to_csv(output_path, index=False)

    report = {
        "raw_rows": raw_rows,
        "exact_duplicate_rows": exact_duplicates,
        "repeated_product_links": repeated_links,
        "cleaned_rows": len(df),
        "cleaned_columns": df.shape[1],
        "original_price_below_current": int((df["Original Price"] < df["Current Price"]).sum()),
        "missing_values": df.isna().sum().to_dict(),
        "output_path": output_path,
    }
    return df, report
