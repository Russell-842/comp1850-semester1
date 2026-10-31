# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def _init__(self, name, birth):
        self.name = name
        self.birth = birth

    try :
         width = int(name("Enter name : "))
         height = int(birth("Enter birth date : "))
    except TypeError :
        if not isinstance(width, (str)):
            raise TypeError("Name must be a string")
        if not isinstance(birth, (date)):
            raise TypeError("Birth date must be a date")


    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
