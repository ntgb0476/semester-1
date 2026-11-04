# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

from point import Point
from shapes import Circle


circle = Circle(Point(0, 0), "red", 2.5)
print(circle)
print(f"Area = {circle.area()}")
print(f"Perimeter = {circle.perimeter()}")
print("Moving the circle...")
circle.set_position(Point(1.6, 3.2))
print(circle)
print("Changing the circle's colour...")
circle.set_colour("green")
print(circle)
