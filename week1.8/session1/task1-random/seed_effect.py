# See README.md for instructions on what to do this program

import random

# Prints 3 random numbers between 1 and 100, with the number argument 
# of the call assigned 3 set numbers
random.seed(10)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)

# Output if random.seed(10) = 74 5 55 - same 3 numbers
# IF random.seed(20) = 93 88 99
# IF random.seed(84) = 94 37 100
# IF random.seed (56) = 72 2 61
# BUT IF # random.seed() = 3 different integers every time
