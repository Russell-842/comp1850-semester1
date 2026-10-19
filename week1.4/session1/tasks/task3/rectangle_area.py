
# function implementation

# 1) Calculate and returns the area of a rectangle
def rectangle_area(width, height):  # define suitable input data
    area = width * height          # implement the function
    return area              # return an appropriate value

# Simpler way of writing expression for area
def rectangle_area(width, height):
    return width * height

# testing the function

print(f"Area is {rectangle_area(2, 5)}")   # provide suitable data matching your inputs

# 2) Accept an integer value and returns a list of even integers between 0 and that value

def even_numbers(limit) :
    evens = []
#  Write a loop
    for n in range(limit + 1) :
        if n % 2 == 0 :
            evens.append(n)
    return evens

print(even_numbers(20))

# SHORTENED way of writing function
def even_numbers(limit) :
    return [ n for n in range(limit+1) if n % 2 == 0]

print(even_numbers(20))

# 3) Accept a list of integers and returns the mean average of the list.
def mean_average(numbers):
    return sum(numbers) / len(numbers)


print(mean_average([1, 2, 3, 4, 5]))
