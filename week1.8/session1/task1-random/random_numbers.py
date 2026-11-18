import random

# Get user to input how many random numbers they want
how_many = int(input("How many random numbers do you want ? "))

# Generate this many random numbers
random.seed() 

# Write the random numbers to a file named random.txt, one number per line
nums = []

for i in range(how_many):
    nums.append(random.randint(1, 100))

print(nums)

