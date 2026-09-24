
def save_report(report):

    with open("sales_report.txt", "w") as file:
        file.write(report)
