# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math


class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        """Returns the point's distance from the origin."""
        return math.hypot(self.x, self.y)

    def distance_to(self, x, y):
        """Returns the points distance to the inputed point."""
        return math.hypot(self.x - x, self.y - y)


# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle


class Circle:
    """
    A shape in 2D space.
    """

    def __init__(self, centre, radius):
        self.radius = radius
        self.centre = centre

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * self.radius * math.pi
