
# Week 4 Retail Sales Analysis

import module1_condition
import module2_loop
import module3_function
import module4_file


# Read the CSV file
sales_data = module4_file.read_sales_file(
    "nepal_retail_sales_dataset.csv"
)


# Calculate total sales
total_sales = module2_loop.calculate_total_sales(
    sales_data
)


# Count male and female customers
male, female = module2_loop.count_gender(
    sales_data
)


# Count product categories
categories = module2_loop.count_categories(
    sales_data
)

popular_category, category_count = module2_loop.find_popular_category(
    categories
)


# Calculate average sales
average_sales = module3_function.calculate_average(
    total_sales,
    len(sales_data)
)


# Compare male and female customers
gender_summary = module1_condition.compare_gender(
    male,
    female
)


# Create final report
report = f"""
==================================================

              RETAIL SALES ANALYSIS

==================================================

Total Transactions       : {len(sales_data)}
Total Sales              : NPR {total_sales:,.2f}
Average Sales            : NPR {average_sales:,.2f}
Male Customers           : {male}
Female Customers         : {female}
Most Popular Category    : {popular_category}
Category Transactions    : {category_count}

{gender_summary}

==================================================
"""


# Save and display report
module4_file.save_report(report)

print(report)
