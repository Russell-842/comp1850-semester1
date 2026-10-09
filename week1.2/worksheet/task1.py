# Worksheet 1.2: Task 1 Solution

# Ask the user to enter an integer grade in the range 0 to 100
grade = int(input("Enter your grade between the range of 0 and 100 : "))
if grade >= 70 and grade <= 100 :
    print(grade,"is a Distinction")
elif grade >= 40 and grade <= 69 :
    print(grade, "is a Pass")
elif grade >= 0 and grade <= 39 :
    print(grade, "is a Fail")
else :
    import sys
    sys.exit("Error : Grade must be an integer between 0 and 100")
# Immediately exit the program if user doesn't enter a number/integer value outside required range
