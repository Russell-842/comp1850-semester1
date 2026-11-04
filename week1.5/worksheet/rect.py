# Worksheet 1.5: Rectangle Class

import math 


class Rectangle :
    """
    A rectangle, with a width and a height.
    """

    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """  
        if not isinstance(width, (int)):
            raise TypeError("Width must be an integer")
        
        if not isinstance(height, (int)):
            raise TypeError("Height must be an integer")

        if width <= 0 or height <= 0:
            raise ValueError("Only positive integers are allowed")

        self.width = width
        self.height = height

    def is_square(self):
        """
        Returns 'True' if the rectangle is actually a square, 'False' othwerwise
        """
        return self.width == self.height

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        return 2 * (self.width + self.height)