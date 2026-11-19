# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle
import math


def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2


def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0


def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)

    assert p1.distance_to(p2) == math.sqrt(3**2 + 4**2)


def test_point_init():
    p = Circle(5, Point(5, -2))
    assert p.area() == math.pi * 5**2
    assert p.perimeter() == math.pi * 2 * 5
