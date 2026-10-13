# Worksheet 1.2: Task 2 Solution

import sys
from util import read_numbers

try:
    numbers = read_numbers()
except ValueError:
    sys.exit("Error: no numbers provided")

if not numbers:
    sys.exit("Error: no numbers provided")

# Finds the minimum, maximum, mean and median of these values
min_value = min(numbers)
max_value = max(numbers)
mean_value = sum(numbers) / len(numbers)

numbers.sort()
n = len(numbers)
if n % 2 == 0:
    median_value = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
else:
    median_value = numbers[n // 2]

# Prints these statistics
print(f"Minimum = {min_value}")
print(f"Maximum = {max_value}")
print(f"Mean = {mean_value}")
print(f"Median = {median_value}")