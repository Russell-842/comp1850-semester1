# Week 4, Session 2: Task 4

# Given an incomplete recursive function power to calculate x raised to
# the power of n, your task is to complete the function.


def power(x, n):
    # complete your code here
    # base case
    if n == 0 :
        return 1
    if n < 0 :
        return 1 / power(x, n)
    # recursive case
    return x * power(x, n - 1)

# Once completed, make at least two function calls to test the power function
if __name__ == "__main__":
    x = 8
    n = 4
    recursive_result = power(x, n)
    print("The recursive result is:", recursive_result) # Output : 4096
