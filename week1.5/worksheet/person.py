# Worksheet 1.5: Person class

from datetime import date


class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    def __init__(self, name, birth):
        if not type(name) is str:
            raise TypeError("Name is not a string.")
        if len(name) == 0:
            raise ValueError("Name is an empty string")
        if not type(birth) is date:
            raise TypeError("Date is not a date")
        self.name = name
        self.birth = birth

    def initials(self): ...

    def is_birthday(self):
        return (
            self.birth.month == date.today().month
            and self.birth.day == date.today().day
        )
