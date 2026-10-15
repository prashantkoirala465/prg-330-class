"""Module 03: Conditional logic applied to real Daraz values only."""

import pandas as pd


def price_group(price):
    """Classify an actual cleaned Daraz price using if/elif/else."""
    if pd.isna(price):
        return "Unknown"
    if price < 500:
        return "Budget"
    elif price < 2000:
        return "Mid"
    else:
        return "Expensive"


def delivery_label(value):
    """Translate the datasource's delivery code into a readable label."""
    if str(value) == "0":
        return "No Free Delivery"
    else:
        return str(value)


def voucher_label(value):
    """Reduce the real voucher field to a Yes/No feature."""
    if str(value) == "0":
        return "No"
    else:
        return "Yes"


def condition_summary(csv_path):
    """Apply conditional rules to the actual datasource and summarize the results."""
    df = pd.read_csv(csv_path)
    prices = pd.to_numeric(df["Current Price"].astype(str).str.replace(",", "", regex=False), errors="coerce")

    price_groups = {"Budget": 0, "Mid": 0, "Expensive": 0, "Unknown": 0}
    for price in prices:
        group = price_group(price)
        price_groups[group] += 1

    delivery_groups = {"Free Delivery": 0, "No Free Delivery": 0}
    for value in df["Delivery"]:
        label = delivery_label(value)
        if label in delivery_groups:
            delivery_groups[label] += 1

    voucher_groups = {"Yes": 0, "No": 0}
    for value in df["Voucher"]:
        voucher_groups[voucher_label(value)] += 1

    return {
        "price_groups_raw_rows": price_groups,
        "delivery_groups_raw_rows": delivery_groups,
        "voucher_groups_raw_rows": voucher_groups,
    }
