# Worksheet 1.2: Task 2 Solution

# Write a program that prompts the user to enter a sequence of 'float' values

numbers = []
try : 
    num1 = float(input("Enter your first value : "))
    num2 = float(input("Enter your second value : "))
    num3 = float(input("Enter your third value : "))
    num4 = float(input("Enter your fourth value : "))
    num5 = float(input("Enter your fifth value : "))

except ValueError :
    print("Error : No numbers provided")
# Reads these values into a list, using the code we have provided
else :
    numbers.append(num1)
    numbers.append(num2)
    numbers.append(num3)
    numbers.append(num4)
    numbers.append(num5)
print(numbers)

# Finds the minimum, maximum, mean and median of these values
min_value = min(numbers)
max_value = max(numbers)
mean_value = sum(numbers) / len(numbers)

numbers.sort()
n = len(numbers)
median_value = numbers[n // 2]

# Prints these statistics
print("Minimum value = ", min_value)
print("Maximum value = ", max_value)
print("Mean value = ", mean_value)
print("Median value = ", median_value)