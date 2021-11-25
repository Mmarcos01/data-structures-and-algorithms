from array_binary_search import binary_search

def test_binary_search_in_mid():
    sorted_list = [1,2,3,4,5]
    value = 3
    actual = binary_search(sorted_list, value)
    assert actual == 2

def test_binary_search_in_higher():
    sorted_list = [1,2,3,4,5]
    value = 5
    actual = binary_search(sorted_list, value)
    assert actual == 4

def test_binary_search_in_lower():
    sorted_list = [1,2,3,4,5]
    value = 2
    actual = binary_search(sorted_list, value)
    assert actual == 1

def test_binary_search_not_found():
    sorted_list = [1,2,3,4,5]
    value = 6
    actual = binary_search(sorted_list, value)
    assert actual == -1

