# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class

from geometry import Point, Circle

circle = Circle(5, Point(3, 3))
point = Point(3, -1)
print(point in circle)
