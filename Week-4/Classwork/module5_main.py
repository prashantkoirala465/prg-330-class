
from data import customers

import module1_condition
import module2_loop
import module3_function
import module4_file


# Conditional Value
print('*' * 10, "High Value Customer", '*' * 10)

for customer in customers:

    result = module1_condition.classify_sale(
        customer["sales"]
    )

    if result == 'High Value':
        print(customer["name"])


# Loop Module
total = module2_loop.calculate_total_sales(customers)

male, female = module2_loop.count_gender(customers)


# Function Module
average = module3_function.calculate_average(
    total,
    len(customers)
)


# Create Report
report = f"""
===================================================

            SALES ANALYSIS REPORT

===================================================

Total Sales        : NPR {total:,.0f}
Average Sales      : NPR {average:,.0f}
Male Customers     : {male}
Female Customers   : {female}

===================================================
"""


# File Module
module4_file.save_report(report)

print(report)
