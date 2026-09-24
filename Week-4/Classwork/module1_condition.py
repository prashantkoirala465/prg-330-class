
def classify_sale(sales):

    if sales >= 50000:
        return "High Value"

    elif sales >= 20000:
        return "Medium Value"

    else:
        return "Regular"
