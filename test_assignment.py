import assignment
import assignment
import time
import pytest

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return execution_time
    return wrapper 


def test_swap_values():
    # Test case 1: List with two elements
    lst = [2, 1]
    assignment.swap_values(lst)
    assert lst == [1, 2]

    # Test case 2: List with three elements
    lst = [3, 1, 2]
    assignment.swap_values(lst)
    assert lst == [1, 3, 2]

    # Test case 3: List with duplicate elements
    lst = [5, 3, 5, 2, 1]
    assignment.swap_values(lst)
    assert lst == [3, 5, 5, 2, 1]

def test_compare_values():
    # Test case 1: List with two elements
    lst = [2, 1]
    result = assignment.compare_values(lst)
    assert result == [True]

    # Test case 2: List with three elements
    lst = [3, 1, 2]
    result = assignment.compare_values(lst)
    assert result == [True, False]

    # Test case 3: List with duplicate elements
    lst = [5, 3, 5, 2, 1]
    result = assignment.compare_values(lst)
    assert result == [True, False, True, True]

@timer_decorator
def sort_list(lst):
    lst.sort()
    

@timer_decorator
def sort_bubble(lst):
    assignment.bubble_sort(lst)


def test_bubble_sort():
    # Test case 1: List with two elements
    lst = [2, 1]
    assignment.bubble_sort(lst)
    assert lst == [1, 2]

    # Test case 2: List with three elements
    lst = [3, 1, 2]
    assignment.bubble_sort(lst)
    assert lst == [1, 2, 3]

    # Test case 3: List with duplicate elements
    lst = [5, 3, 5, 2, 1]
    assignment.bubble_sort(lst)
    assert lst == [1, 2, 3, 5, 5]

    # Test case 4: Test that the .sort() method is not used
    lst = [5, 3, 5, 2, 1]

    time_assignment = sort_bubble(lst)
    time_sort = sort_list(lst)

    assert time_assignment > time_sort


