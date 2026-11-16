import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

print(names)

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

how_many = int(input("How many names ? "))

choices = random.sample(names, how_many)

# Display the chosen names, one per line
for choice in choices :
    print(choices)
