# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Check pounds parameter is an integer
        if not isinstance(pounds, int):
            raise TypeError("Pounds must be an integer.")
        # Check pounds is not negative
        if pounds < 0:
            raise ValueError("Pounds cannot be negative.")
        # Check pence parameter is an integer
        if not isinstance(pence, int):
            raise TypeError("Pence must be an integer.")
        # Check pence is not negative and not greater than 99
        if pence < 0 or pence > 99:
            raise ValueError("Pence must be between 0 and 99.")

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # Return an appropriate string representation with currency for British Pounds Sterling and leading zero for pence
        return f"£{self.pounds}.{self.pence:02d}"

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        # Check paramter 'other' is a Money object
        if not isinstance(other, Money):
            raise TypeError("Not a Money object")
        # Add self to other, then return sum as a new Money object 
        sum_pounds = self.pounds + other.pounds
        extra_pound = (self.pence + other.pence) // 100
        sum_pence = (self.pence + other.pence) % 100

        return Money(sum_pounds + extra_pound, sum_pence)
