# there are several errors in this code
# run the code, read the error messages or look at the output, and fix the problems

# Find and fix the errors

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = str(input("Enter your city: "))

print(f"Hello {name}, you are {age} years old and live in {city}.")

try :
    num1 = int(input("Enter your number : "))
    num2 = int(input("Enter your number : "))
    answer = num1 + num2
    print(f"{num1} + {num2} = {answer}")
except :
    print("Please enter numbers only")    

