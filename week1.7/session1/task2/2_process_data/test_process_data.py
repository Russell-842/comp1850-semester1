# Week 1.7, Session 1: Task 2 - unit test for process_data() 

# Write test functions for the values you have chosen in the equivalence classes
# for testing the functions

# Hint: you should test for empty list, list with a single value, list with multiple values
# and for positive and negative integers


from process_data import process_data

# Implementation for testing an empty list
# Says to return None if no data
def test_empty_list():
    assert process_data([]) is None
    
# Implementation for testing a list with a single integer
def test_one_int_list():
    assert process_data([1]) == 1

# Implementation for testing a list with multiple integers
def test_multiple_int_list():
    assert process_data([1, 2, 3]) == 6

    # Implementation for testing a list with negative integers
def test_negative_int_list():
    assert process_data([-1, -2, -3]) == -6

    # Implementation for testing a list with mixed integers
def test_mixed_int_list():
    assert process_data([-1, 2, -3]) == -2


    
    
