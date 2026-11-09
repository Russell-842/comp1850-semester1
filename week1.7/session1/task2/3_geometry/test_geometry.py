# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0

# Implementation for testing distance_to()
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
# Assertion between 2 different points
    assert p1.distance_to(p2) == 5.0

# Write test functions to test the __init__() in Circle class
# Use default value for centre coordinates

def test_circle_constructor():
    circle = Circle(2.0)
    assert circle.radius == 2.0
    assert circle.centre.x == 0.0
    assert circle.centre.y == 0.0
    circle2 = Circle(4.0, Point(1.0, 2.0))
    assert circle2.radius == 4.0
    assert circle2.centre.x == 1.0
    assert circle2.centre.y == 2.0

# Test functions to test area() and perimeter() methods in Circle Class
def test_area():
    circle = Circle(2.0)
#   assert circle.area() ==

def test_perimeter():
    circle = Circle(2.0)
#   assert circle.perimeter ==
