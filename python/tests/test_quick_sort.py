import pytest
from sorting.quick_sort import quick_sort

def test_quick_sort():
    list = [8,4,23,42,16,15]
    n = len(list)
    actual = quick_sort(list, 0, n - 1)
    expected = [4,8,15,16,23,42]
    assert actual == expected

# def test_quick_sort_reverse_sorted():
#     list = [20,18,12,8,5,-2]
#     n = len(list)
#     actual = quick_sort(list, 0, n - 1)
#     expected = [-2,5,8,12,18,20]
#     assert actual == expected

# def test_quick_sort_multiples():
#     list = [5,12,7,5,5,7]
#     n = len(list)
#     actual = quick_sort(list, 0, n - 1)
#     expected = [5,5,5,7,7,12]
#     assert actual == expected

# def test_quick_sort_nearly_sorted():
#     list = [2,3,5,7,13,11]
#     n = len(list)
#     actual = quick_sort(list, 0, n - 1)
#     expected = [2,3,5,7,11,13]
#     assert actual == expected
