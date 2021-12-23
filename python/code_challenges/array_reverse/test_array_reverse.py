from array_reverse import rev_list, rev_list2, rev_list3

def test_reverse():
    list = [1,2,3,4,5]
    actual = rev_list(list)
    assert actual == [5,4,3,2,1]

def test_reverse2():
    list = ['cat', 'dog', 'turtle']
    actual = rev_list(list)
    assert actual == ['turtle', 'dog', 'cat']

def test_rev_list2():
    list = [1,2,3,4,5]
    actual = rev_list2(list)
    assert actual == [5,4,3,2,1]

def test_rev_list3():
    list = [1,2,3,4,5]
    actual = rev_list2(list)
    assert actual == [5,4,3,2,1]
