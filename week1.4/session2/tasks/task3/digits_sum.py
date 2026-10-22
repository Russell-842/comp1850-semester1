# Week 4, Session 2: Task 4

# Given incomplete recursive function digits_sum with a docstring,
# your task is to complete the function based on the description


def digits_sum(number):
    """
    This recursive function calculates the sum of digits of a given positive
    integer. For example, sum of digits for 987 = 9 + 8 + 7 = 24.
    For simplicity, ignore the case when number is not an integer or
    not a positive integer.

    Args:
        number (int): The input is a positive integer.

    Returns:
        int: The sum of the digits of the input integer.
    """
    # Complete your code here
def digits_sum(number):
    # Base Case = If number is 0, return 0
    if number == 0 :
        return 0
    # Recursive case = Calculating the sum of digits of a given positive integer
    return (number % 10 + digits_sum(int(number / 10)))

# check if correct output is produced
print(digits_sum(987))  # Output: 24
print(digits_sum(12345))  # Output: 15

# Once completed, your next task is to write an equivalent function that uses loops.
