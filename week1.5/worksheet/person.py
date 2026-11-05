# Worksheet 1.5: Person class

from datetime import date


class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    def __init__(self, name, birth):
        """
        Init's the class.
        """
        if not type(name) is str:
            raise TypeError("Name is not a string.")
        if len(name) == 0:
            raise ValueError("Name is an empty string")
        if not type(birth) is date:
            raise TypeError("Date is not a date")
        self.name = name
        self.birth = birth

    def initials(self):
        """
        Returns the initals of the person's name
        """
        output = []
        for name in self.name.split():
            output.append(name[0])
        return "".join(output).upper()

    def is_birthday(self):
        """
        Returns true if today is the person's birthday.
        """
        return (
            self.birth.month == date.today().month
            and self.birth.day == date.today().day
        )
