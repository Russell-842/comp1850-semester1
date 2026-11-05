# Worksheet 1.5: Person class

from datetime import date


class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name, birth):
        """
        Creates values for a Person, using given name and birth date
        """
        
        if not isinstance(name, (str)):
            raise TypeError("Name must be a string")
    
        if not isinstance(birth, (date)):
            raise TypeError("Birth date must be a 'date' object")

        if name == "" :
            raise ValueError("The 'name' value should not be empty")

        self.name = name
        self.birth = birth

    def initials(self):
        """
    Returns uppercased initial letters of person's name
        """
        return "".join(word[0].upper() for word in 
    self.name.split())

    def is_birthday(self):
        """
    Returns 'True' if today is person's birthday and 'False' otherwise
        """
        today = date.today()

        return (
        today.day == self.birth.day 
        and today.month == self.birth.month
        )
        

