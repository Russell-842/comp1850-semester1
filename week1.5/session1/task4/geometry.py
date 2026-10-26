# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates
        """
        self.x = x
        self.y = y

# Add a definition for a Circle class here, giving it
class Circle : 
    """
    A circle with radius and centre
    """
    def __init__(self, radius, centre=Point(0.0,0.0)) :
        self.radius = radius
        self.centre = centre

# - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
    def centre(self) :
        return self.centre
# - A method area(), returning the area of the circle
    def area(self) :
        """
        Returns the area of the circle
        """
        return math.pi * self.radius * self.radius

#  - A method perimeter(), returning the perimeter of the circle
    def perimeter(self) :
        """
        Returns the perimeter (circumference) of the circle
        """
        return 2 * math.pi * self.radius
    
# Don't add any testing code to this file!