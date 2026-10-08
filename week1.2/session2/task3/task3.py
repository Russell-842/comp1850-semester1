# Week 1.2, Session 2: Task 3
# Simple Voting Eligibility Checker

# Prompt the user to enter their age

age = int(input("Enter your age: "))

# Use an if statement to check if the user is 18 or over (greater than or equal to 18)
# (Replace XXX with a suitable boolean expression)
# Use 'len' for strings and 'int for integers

if int(age) >= 18 :
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
