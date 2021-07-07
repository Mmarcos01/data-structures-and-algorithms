from stacks_queues.stacks_queues import Node, Stack, Queue

def test_stack_isEmpty():
    my_stack = Stack()
    actual = my_stack.isEmpty()
    expected = True
    assert actual == expected

def test_stack_push_multiple():
    my_stack = Stack()
    my_stack.push('a')
    my_stack.push('b')
    actual = my_stack.__str__()
    expected = "{'b'} -> {'a'} -> None"
    assert actual == expected

def test_stack_pop():
    my_stack = Stack()
    my_stack.push('a')
    my_stack.push('b')
    my_stack.push('c')
    my_stack.pop()
    actual = my_stack.top.value
    expected = 'b'
    assert actual == expected

def test_stack_peek():
    my_stack = Stack()
    my_stack.push('test')
    my_stack.push('new')
    actual = my_stack.peek()
    expected = 'new'
    assert actual == expected

def test_queue_isEmpty():
    my_queue = Queue()
    actual = my_queue.isEmpty()
    expected = True
    assert actual == expected

def test_enqueue():
    my_queue = Queue()
    my_queue.enqueue('a')
    my_queue.enqueue('b')
    my_queue.enqueue('c')
    actual = my_queue.rear.value
    expected = 'c'
    assert actual == expected

def test_dequeue():
    my_queue = Queue()
    my_queue.enqueue('a')
    my_queue.enqueue('b')
    my_queue.enqueue('c')
    actual = my_queue.dequeue()
    expected = 'b'
    assert actual == expected

def test_queue_peek():
    my_queue = Queue()
    my_queue.enqueue('a')
    my_queue.enqueue('b')
    actual = my_queue.peek()
    expected = 'a'
    assert actual == expected
