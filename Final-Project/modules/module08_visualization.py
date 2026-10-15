"""Module 08: Matplotlib visualizations created only from real Daraz data."""

import pandas as pd
import matplotlib.pyplot as plt
from module03_conditions import price_group


def _load_analysis_data(cleaned_csv_path):
    df = pd.read_csv(cleaned_csv_path)
    if "Price Group" not in df.columns:
        df["Price Group"] = [price_group(price) for price in df["Current Price"]]
    return df


def plot_category_overview(cleaned_csv_path):
    df = _load_analysis_data(cleaned_csv_path)

    counts = df["Category"].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index, counts.values, edgecolor="white", width=0.7)
    plt.title("Number of Products in Each Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Products")
    plt.xticks(rotation=30, ha="right")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()

    prices = df.groupby("Category")["Current Price"].median().sort_values()
    plt.figure(figsize=(10, 6))
    plt.barh(prices.index, prices.values, edgecolor="white")
    plt.title("Median Current Price by Category")
    plt.xlabel("Median Current Price (Rs)")
    plt.ylabel("Category")
    plt.grid(axis="x", alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_price_distribution(cleaned_csv_path):
    df = _load_analysis_data(cleaned_csv_path)

    groups = df["Price Group"].value_counts()
    plt.figure(figsize=(7, 7))
    plt.pie(groups.values, labels=groups.index, autopct="%1.1f%%", explode=[0.05] + [0] * (len(groups) - 1))
    plt.title("Share of Products in Each Price Group")
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.hist(df["Current Price"], bins=40, edgecolor="white")
    plt.title("Price Distribution of All Products")
    plt.xlabel("Price in Rs")
    plt.ylabel("Number of Products")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_sales_and_ratings(cleaned_csv_path):
    df = _load_analysis_data(cleaned_csv_path)

    sold = df.groupby("Category")["Sold Count"].median().sort_values()
    plt.figure(figsize=(10, 6))
    plt.barh(sold.index, sold.values, edgecolor="white")
    plt.title("Median Sold Count by Category")
    plt.xlabel("Median Reported Units Sold")
    plt.ylabel("Category")
    plt.grid(axis="x", alpha=0.3)
    plt.tight_layout()
    plt.show()

    ratings = df.groupby("Category")["Rating in Stars"].mean().sort_values()
    plt.figure(figsize=(10, 6))
    plt.barh(ratings.index, ratings.values, edgecolor="white")
    plt.title("Average Star Rating by Category (Rated Products Only)")
    plt.xlabel("Rating out of 5")
    plt.ylabel("Category")
    plt.xlim(0, 5)
    plt.grid(axis="x", alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_relationships(cleaned_csv_path):
    df = _load_analysis_data(cleaned_csv_path)

    relationships = [
        ("Current Price", "Price vs Sold Count", "Price in Rs"),
        ("Rating Count", "Rating Count vs Sold Count", "Number of Ratings"),
        ("Discount %", "Discount Percentage vs Sold Count", "Discount Percentage"),
    ]

    correlations = {}
    for x_column, title, xlabel in relationships:
        plot_data = df.dropna(subset=[x_column, "Sold Count"])
        plt.figure(figsize=(10, 6))
        plt.scatter(plot_data[x_column], plot_data["Sold Count"], alpha=0.45, edgecolor="white", linewidth=0.3)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel("Reported Units Sold")
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.show()
        correlations[x_column] = float(plot_data[x_column].corr(plot_data["Sold Count"]))

    return correlations


def plot_promotion_comparisons(cleaned_csv_path):
    df = _load_analysis_data(cleaned_csv_path)

    delivery = df.groupby("Delivery")["Sold Count"].median()
    voucher = df.groupby("Has Voucher")["Sold Count"].median()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.bar(delivery.index, delivery.values, edgecolor="white")
    ax1.set_title("Median Sold Count by Free-Delivery Status")
    ax1.set_xlabel("Delivery Status")
    ax1.set_ylabel("Reported Units Sold")
    ax1.grid(axis="y", alpha=0.3)

    ax2.bar(voucher.index, voucher.values, edgecolor="white")
    ax2.set_title("Median Sold Count by Voucher Status")
    ax2.set_xlabel("Has Voucher")
    ax2.set_ylabel("Reported Units Sold")
    ax2.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()

    voucher_by_category = df.pivot_table(
        index="Category", columns="Has Voucher", values="Sold Count", aggfunc="median"
    )
    voucher_counts = df.pivot_table(
        index="Category", columns="Has Voucher", values="Title", aggfunc="count", fill_value=0
    )

    voucher_by_category.plot(kind="bar", figsize=(11, 6), edgecolor="white")
    plt.title("Median Sold Count With and Without Vouchers, by Category")
    plt.xlabel("Category")
    plt.ylabel("Reported Units Sold")
    plt.xticks(rotation=30, ha="right")
    plt.legend(title="Has Voucher")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()

    return voucher_counts
