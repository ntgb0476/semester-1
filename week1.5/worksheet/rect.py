# Worksheet 1.5: Rectangle Class


class Rectangle:
    """
    A rectangle, with a width and a height.
    """

    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not type(width) is int:
            raise TypeError("Width is not an int.")
        if not type(height) is int:
            raise TypeError("Height is not an int.")
        if width <= 0 or height <= 0:
            raise ValueError("Inputed values for rectangle must be greater then zero.")
        if type(width) != int:
            print("Oh no")
            print(type(width))
        self.width = width
        self.height = height

    def is_square(self):
        """
        Returns true if the rect is a square
        """
        return self.width == self.height

    def area(self):
        """
        Returns the area of the square
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the square
        """
        return 2 * (self.width + self.height)
