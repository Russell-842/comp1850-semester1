# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")

# All lowercase
print(f"Modified String 1: {user_string.lower()}")

# All uppercase
print(f"Modified String 2: {user_string.upper()}")

# Removes any spaces/specified characters
print(f"Modified String 3: {user_string.strip()}")

# Replaces all 'a' with '@'
print(f"Modified String 4: {user_string.replace('a', '@')}")

# Capital letter at the start
print(f"Modified String 5: {user_string.capitalize()}")

# Switches order of letters (starts from backwards)
print(f"Modified String 6: {user_string[::-1]}")

# Capital letter at the start of every character/word
print(f"Modified String 7: {user_string.title()}")

# Shows how many letters there are
print(f"Modified String 8: {len(user_string)}")

# Counts how many characters there are before 'a' appears
print(f"Modified String 9: {user_string.find('a')}")

# Counts how many times 'a' is part of string
print(f"Modified String 10: {user_string.count('a')}")

# True/False if it starts with 'Hello'
print(f"Modified String 11: {user_string.startswith('Hello')}")

# True/False if it ends with '!'
print(f"Modified String 12: {user_string.endswith('!')}")

# True/False if contains only alphanumeric characters e.g letter (a-z) or number (0-9)
print(f"Modified String 13: {user_string.isalnum()}")

# True/False determining if all characters are alphabetic (a-z)
print(f"Modified String 14: {user_string.isalpha()}")

# True/False if it is a digit
print(f"Modified String 15: {user_string.isdigit()}")

######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!