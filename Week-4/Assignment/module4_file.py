
# Module 4 - File input and output

import csv


def read_sales_file(filename):

    sales_data = []

    with open(filename, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            sales_data.append(row)

    return sales_data


def save_report(report):

    with open("sales_report.txt", "w") as file:
        file.write(report)
