# Week 1.7, Session 1: Task 4 - unit tests for methods in Money

import pytest

from money import Money

def test_invalid_type_pound():
    with pytest.raises(TypeError) as excinfo:
        Money(1.2, 99)
    assert str(excinfo.value) == "pounds must be an integer"


def test_invalid_value_pound():
    with pytest.raises(ValueError) as excinfo:
        Money(-1, 0)
    assert str(excinfo.value) == "pounds must be >= 0"


def test_add_invalid_type():
    m1 = Money(5, 0)
    with pytest.raises(TypeError) as excinfo:
        m1 + 42
    assert str(excinfo.value) == "other object must be a Money"

# Test implementation for invalid type for pence (TypeError)
def test_invalid_type_pence():
# Raise TypeError when pence cannot be converted to a number
    with pytest.raises(TypeError) :
        Money(1, 5.0)
    

def test_pence_negative():
# Raise ValueError when it is negative; convert valid input to Decimal for reliable price handling
    with pytest.raises(ValueError) :
        Money(1, -1)
            

def test_valid_add():
    m1 = Money(1, 50)
    m2 = Money(0, 54)
    assert str(m1 + m2) == "£2.04"
