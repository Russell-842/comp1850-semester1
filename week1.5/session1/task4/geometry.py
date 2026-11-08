# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

class Point:
    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates
        """
        self.x = x
        self.y = y

class Circle : 
    """
    A circle with radius and centre
    """
    def __init__(self, radius, centre=Point(0.0,0.0)) :
        self.radius = radius
        self.centre = centre

    def centre(self) :
        return self.centre
    
    def area(self) :
        """
        Returns the area of the circle
        """
        return math.pi * self.radius * self.radius

    def perimeter(self) :
        """
        Returns the perimeter (circumference) of the circle
        """
        return 2 * math.pi * self.radius
    
