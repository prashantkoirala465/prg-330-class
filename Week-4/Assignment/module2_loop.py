
# Module 2 - Loop statements

def calculate_total_sales(sales_data):

    total = 0

    for item in sales_data:
        total = total + float(item["Sales_NPR"])

    return total


def count_gender(sales_data):

    male = 0
    female = 0

    for item in sales_data:

        if item["Customer_Gender"] == "Male":
            male = male + 1

        elif item["Customer_Gender"] == "Female":
            female = female + 1

    return male, female


def count_categories(sales_data):

    categories = {}

    for item in sales_data:

        category = item["Product_Category"]

        if category in categories:
            categories[category] = categories[category] + 1

        else:
            categories[category] = 1

    return categories


def find_popular_category(categories):

    popular_category = ""
    highest_count = 0

    for category in categories:

        if categories[category] > highest_count:
            highest_count = categories[category]
            popular_category = category

    return popular_category, highest_count
