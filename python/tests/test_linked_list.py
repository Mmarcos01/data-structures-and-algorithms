from linked_list.linked_list import LinkedList, Node

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

# def test_insert():
#     node = Node('blue', None)
#     insert_node = Node('red', node)
#     actual = insert_node.next.value
#     expected = 'blue'
#     assert actual == expected

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
    my_list = LinkedList(Node('green', Node('blue', Node ('red'))))
    my_list.append('orange')
    actual = my_list.__str__()
    expected = "{'green'} -> {'blue'} -> {'red'} -> {'orange'} -> None"
    assert actual == expected

def test_insertAfter():
    my_list = LinkedList(Node('green', Node('blue', Node ('red'))))
    my_list.insertAfter('blue', 'orange')
    actual = my_list.__str__()
    expected = "{'green'} -> {'blue'} -> {'orange'} -> {'red'} -> None"
    assert actual == expected

def test_insertBefore():
    my_list = LinkedList(Node('green', Node('blue', Node ('red'))))
    my_list.insertBefore('blue', 'orange')
    actual = my_list.__str__()
    expected = "{'green'} -> {'orange'} -> {'blue'} -> {'red'} -> None"
    assert actual == expected
