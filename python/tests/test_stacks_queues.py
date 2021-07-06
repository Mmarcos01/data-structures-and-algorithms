from stacks_queues.stacks_queues import Node, Stack

def test_isEmpty():
    my_stack = Stack()
    actual = my_stack.__str__()
    expected = "None"
    assert actual == expected

def test_push():
    my_stack = Stack(Node('a', Node('b', Node ('c'))))
    my_stack.push('d')
    my_stack.push('e')
    actual = my_stack.__str__()
    expected = "{'a'} -> {'b'} -> {'c'} -> {'d'} -> {'e'} -> None"
    assert actual == expected

def test_pop():
    my_stack = Stack(Node('a', Node('b', Node ('c'))))
    my_stack.pop()
    actual = my_stack.__str__()
    expected = "{'a'} -> {'b'} -> None"
    assert actual == expected
