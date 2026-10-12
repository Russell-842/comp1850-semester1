# Worksheet 1.2: Task 2 Solution

# Write a program that prompts the user to enter a sequence of 'float' values

numbers = []
float()
try : 
    number1 = float(input("Enter your first value : "))
    number2 = float(input("Enter your second value : "))
    number3 = float(input("Enter your third value : "))
    number4 = float(input("Enter your fourth value : "))
    number5 = float(input("Enter your fifth value : "))

except ValueError :
    print("Error : No numbers provided")

# Reads these values into a list, using the code we have provided
# Finds the minimum, maximum, mean and median of these values
# Prints these statistics
