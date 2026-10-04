"""Reusable helper functions for the modular Daraz analysis project."""
import pandas as pd


def sold_to_number(text):
    """Convert Daraz sold-count text such as '6K Sold' or '452 Sold' to a number."""
    if pd.isna(text):
        return None

    text = str(text).replace(" Sold", "")
    if "K" in text:
        return float(text.replace("K", "")) * 1000
    return float(text)


def price_group(price):
    """Classify a current price into analyst-defined Budget, Mid, or Expensive groups."""
    if price < 500:
        return "Budget"
    elif price < 2000:
        return "Mid"
    return "Expensive"
