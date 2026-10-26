# A bad class implementation

# What does the runtime error mean?
# __init__ accepts 1 argument besides self, but the call supplies 2

# How do we fix the code?
# Add 'self' after def __init__ and for self.x and self.y (used as prefix)

# REMEMBER : DOUBLE underscores before AND after init

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate


p = Point(1.5, 2.0)
print(p.x)
print(p.y)
