import pytest
from linked_list.linked_list import LinkedList, Node, zipLists

def test_import():
    assert LinkedList

def test_empty_linked_list():
    empty = LinkedList()
    assert empty

def test_instantiate_node():
    node = Node('green', None)
    actual = node.value
    expected = 'green'
    assert actual == expected
    assert node.next == None

# needs a node included, and a node to insert linked list is already instantiated inside the class method
# def test_insert():
#     node = Node('blue', None)
#     insert_node = Node('red', node)
#     actual = insert_node.next.value
#     expected = 'blue'
#     assert actual == expected

def test_insert():
    linklist = LinkedList()
    linklist.insert("a")
    actual = linklist.head.value
    expected = "a"
    assert actual == expected

def test_includes_and_inserts():
    ll1 = LinkedList()
    ll1.insert('red')
    ll1.insert('blue')
    ll1.insert('green')
    actual =  ll1.includes('red')
    expected = True
    assert actual == expected

def test_to_string():
    ll1 = LinkedList()
    ll1.insert('red')
    ll1.insert('blue')
    ll1.insert('green')
    actual = ll1.__str__()
    expected = "{'green'} -> {'blue'} -> {'red'} -> None"
    assert actual == expected

def test_append():
    my_list = LinkedList()
    my_list.append('orange').append('purple')
    actual = my_list.__str__()
    expected = "{'orange'} -> {'purple'} -> None"
    assert actual == expected

def test_insertAfter():
    # my_list = LinkedList(Node('green', Node('blue', Node ('red'))))
    my_list = LinkedList()
    my_list.append('green').append('blue').append('red')
    my_list.insertAfter('blue', 'orange')
    actual = my_list.__str__()
    expected = "{'green'} -> {'blue'} -> {'orange'} -> {'red'} -> None"
    assert actual == expected

def test_insertBefore():
    # my_list = LinkedList(Node('green', Node('blue', Node ('red'))))
    my_list = LinkedList()
    my_list.append('green').append('blue').append('red')
    my_list.insertBefore('blue', 'orange')
    actual = my_list.__str__()
    expected = "{'green'} -> {'orange'} -> {'blue'} -> {'red'} -> None"
    assert actual == expected

def test_empty_linked_list():
    empty = LinkedList()
    assert empty

def test_k_is_greater_than_ll_length():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d").append("e")
    actual = ll1.kth_from_the_end(2)
    expected = "c"
    assert actual == expected

def test_k_and_the_length_of_the_list_are_the_same():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d").append("e")
    actual = ll1.kth_from_the_end(5)
    expected = "a"
    assert actual == expected

def test_k_is_negative():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d").append("e")
    actual = ll1.kth_from_the_end(-5)
    expected = "K is negative"
    assert actual == expected

def test_linked_list_is_of_a_size_1():
    ll1 = LinkedList()
    ll1.append("a")
    actual = ll1.kth_from_the_end(1)
    expected = "a"
    assert actual == expected

def test_k_is_somewhere_in_the_middle_of_the_linked_list():
    ll1 = LinkedList()
    ll1.append("a").append("b").append("c").append("d").append("e")
    actual = ll1.kth_from_the_end(3)
    expected = "b"
    assert actual == expected

def test_zip_two_lists():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.append("a").append("c").append("e")
    ll2.append("b").append("d").append("f")
    actual = zipLists(ll1,ll2)
    expected = "{'a'} -> {'b'} -> {'c'} -> {'d'} -> {'e'} -> {'f'} -> None"
    assert str(actual) == expected

def test_zip_two_lists_different_sizes():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.append("a").append("c").append("e")
    ll2.append("b")
    actual = zipLists(ll1,ll2)
    expected = "{'a'} -> {'b'} -> {'c'} -> {'e'} -> None"
    assert str(actual) == expected

def test2_zip_two_lists_different_sizes():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.append("a").append("c").append("e")
    ll2.append("b").append("d").append("f").append("g")
    actual = zipLists(ll1,ll2)
    expected = "{'a'} -> {'b'} -> {'c'} -> {'d'} -> {'e'} -> {'f'} -> None"
    assert str(actual) == expected
