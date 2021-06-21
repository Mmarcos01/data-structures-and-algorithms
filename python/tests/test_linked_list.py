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

def test_insert():
    node = Node('blue', None)
    insert_node = Node('red', node)
    actual = insert_node.next.value
    expected = 'blue'
    assert actual == expected

# def test_includes():
#     linked_list = LinkedList(Node())
