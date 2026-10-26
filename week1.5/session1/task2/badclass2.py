# Another bad class implementation

# What does the runtime error mean?
# 'Point' objext has no attribute 'x' as it has not been defined

# How do we fix the code?
# Add 'self' (as a prefix) to make self.x and self.y

# REMEMBER : DOUBLE underscores before AND after init

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates
        """
        self.x = x_coordinate
        self.y = y_coordinate


p = Point(1.5, 2.0)
print(p.x)
print(p.y)
