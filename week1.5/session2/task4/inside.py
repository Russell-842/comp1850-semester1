# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class

from geometry import Point, Circle
point = Point(1.0, 1.5)
circle = Circle(2.5)

if point in circle :
    print("The point lies inside the circle!")
else :
    print("The point lies outside the circle!")