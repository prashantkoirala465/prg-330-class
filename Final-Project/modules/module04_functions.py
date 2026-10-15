"""Module 04: Reusable functions for cleaning real Daraz fields."""

import pandas as pd


def clean_current_price(value):
    """Convert a Current Price value from the datasource to numeric."""
    if pd.isna(value):
        return None
    return pd.to_numeric(str(value).replace(",", ""), errors="coerce")


def clean_original_price(value):
    """Remove Rs. and commas from Original Price and convert to numeric."""
    if pd.isna(value):
        return None
    text = str(value).replace("Rs. ", "").replace(",", "")
    return pd.to_numeric(text, errors="coerce")


def clean_rating(value, rating_count):
    """Convert '4.6/5' to 4.6; unrated products become missing, not 0-star."""
    if pd.isna(value):
        return None
    rating = pd.to_numeric(str(value).replace("/5", ""), errors="coerce")
    if rating_count == 0:
        return None
    return rating


def sold_to_number(value):
    """Convert values such as '6K Sold' to 6000 using real datasource formatting."""
    if pd.isna(value):
        return None

    text = str(value).replace(" Sold", "").strip()
    if "K" in text:
        return float(text.replace("K", "")) * 1000
    else:
        return float(text)


def calculate_discount(original_price, current_price):
    """Return discount amount and percentage from real cleaned prices."""
    if pd.isna(original_price) or pd.isna(current_price) or original_price == 0:
        return None, None
    discount = original_price - current_price
    discount_percent = (discount / original_price) * 100
    return discount, discount_percent


def function_preview(csv_path, n=5):
    """Apply the reusable functions to the first n REAL rows from the datasource."""
    df = pd.read_csv(csv_path).head(n).copy()
    preview = pd.DataFrame({
        "Raw Current Price": df["Current Price"],
        "Clean Current Price": df["Current Price"].apply(clean_current_price),
        "Raw Sold Count": df["Sold Count"],
        "Clean Sold Count": df["Sold Count"].apply(sold_to_number),
        "Raw Rating": df["Rating in Stars"],
        "Clean Rating": [clean_rating(v, c) for v, c in zip(df["Rating in Stars"], df["Rating Count"])],
    })
    return preview
