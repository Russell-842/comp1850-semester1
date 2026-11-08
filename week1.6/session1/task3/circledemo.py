# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

# Import circle and point
from point import Point
from shapes import Circle

# Create a 'Circle' object and print
c = Circle(2.5, Point(0.0, 0.0))

print(c)

# Print circle's area and perimeter, to 3 decimal places
print(f"Area = {c.area():.3f}")
print(f"Perimeter = {c.perimeter():.3f}")

# Change position of circle and print again
print("Moving the circle...")
c.set_position(Point(1.6, 3.2))
print(c)

# Change colour of cirlce and print again
print("Changing the circle's colour...")
c.set_colour("green")
print(c)