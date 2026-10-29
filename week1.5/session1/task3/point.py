# Week 1.5, Session 1: Task 3
import math


class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Add distance() method here
    def distance(self):
        """Returns the point's distance from the origin."""
        return math.hypot(self.x, self.y)

    # Add distance_to() method here
    def distance_to(self, x, y):
        """Returns the points distance to the inputed point."""
        return math.hypot(self.x - x, self.y - y)

    # (This will need a parameter representing another point)


# Finally, add code here to demonstrate use of Point
point = Point(2, 3)
print(point.distance())
print(point.distance_to(4, 7))
