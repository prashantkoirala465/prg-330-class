

def calculate_total_sales(customers):
    total = 0

    for customer in customers:
        total += customer["sales"]

    return total

def count_gender(customers):
    male = 0
    female = 0
    
    for customer in customers:
        if customer["gender"] == "Male":
            male += 1

        elif customer["gender"] == "Female":
            female +=1

    return male, female
