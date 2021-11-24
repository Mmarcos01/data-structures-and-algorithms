from array_shift import array_shift

def test_array_shift_even_array():
    list = [1,2,3,4]
    value = 8
    actual = array_shift(list, value)
    assert actual == [1,2, 8, 3,4]

def test_array_shift_odd_array():
    list = [1,2,3,4,5]
    value = 8
    actual = array_shift(list, value)
    assert actual ==[1,2,3,8,4,5]
