""""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name : Russell Gonzales
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
try :   
    num = int(input("Enter your monthly savings amount : "))
# Validate that they have entered an integer.
except : 
    print("Invalid amount")
    exit()

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
answer = num * 12
# print this out for the user with a suitable message.
print(f"You will save £{answer} by the end of the year")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
answer2 = (((answer / 100) * 0.8) + answer)
# print this out in the format £X.XX (to two decimal places).
print(f"With interest, you will have saved £{answer2:.2f} in a year")