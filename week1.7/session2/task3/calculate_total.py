# Week 1.7, Session 2: Task 3

def calculate_total(price, tax_rate):
    print("Calculating total...")
    tax = price * tax_rate
    total = price + tax
    return total

# Change string "20" to 20, to convert to a number
item_price = 20
tax_percentage = 0.05

final_amount = calculate_total(item_price, tax_percentage)
print(f"Final Amount : {final_amount}")
