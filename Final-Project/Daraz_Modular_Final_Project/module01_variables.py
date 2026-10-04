"""Module 01: Variables and data types using the real Daraz datasource only."""

import pandas as pd


def inspect_variables(csv_path):
    """Read the real datasource and return variables that describe it."""
    df = pd.read_csv(csv_path)

    row_count = df.shape[0]
    column_count = df.shape[1]
    column_names = df.columns.tolist()
    category_count = df["Category"].nunique(dropna=True)
    categories = df["Category"].dropna().unique().tolist()
    data_types = df.dtypes.astype(str).to_dict()
    first_real_title = df.loc[df.index[0], "Title"] if len(df) else None

    return {
        "row_count": row_count,
        "column_count": column_count,
        "column_names": column_names,
        "category_count": category_count,
        "categories": categories,
        "data_types": data_types,
        "first_real_title": first_real_title,
    }
