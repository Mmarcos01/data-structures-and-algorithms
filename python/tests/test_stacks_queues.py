from stacks_queues.stacks_queues import Node, Stack, Queue, PseudoQueue

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

# returns new front after initial front removed
def test_dequeue():
    my_queue = Queue()
    my_queue.enqueue('a')
    my_queue.enqueue('b')
    my_queue.enqueue('c')
    my_queue.enqueue('d')
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

def test_pseudo_enqueue_single():
    my_pseudo = PseudoQueue()
    my_pseudo.enqueue(5)
    actual = my_pseudo.stack1.top.value
    expected = 5
    assert actual == expected

def test_pseudo_enqueue_multiple():
    my_pseudo = PseudoQueue()
    my_pseudo.enqueue(10)
    my_pseudo.enqueue(15)
    my_pseudo.enqueue(20)
    actual = my_pseudo.stack1.top.value
    expected = 20
    assert actual == expected

# pseudo dequeue returns removed rear
def test_pseudo_dequeue():
    my_pseudo = PseudoQueue()
    my_pseudo.enqueue('a')
    my_pseudo.enqueue('b')
    my_pseudo.enqueue('c')
    actual = my_pseudo.dequeue()
    expected = 'a'
    assert actual == expected
