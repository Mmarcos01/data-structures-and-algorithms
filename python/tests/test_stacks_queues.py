import pytest
from stacks_queues.stacks_queues import Node, Stack, Queue, PseudoQueue, AnimalShelter, Dog, Cat

def test_instantiate_empty_node():
    node1 = Node(1)
    assert node1.value == 1
    assert node1.next == None

# ======== Stack ========

def test_stack_is_empty():
    my_stack = Stack()
    actual = my_stack.is_empty()
    expected = True
    assert actual == expected

def test_stack_is_not_empty():
    my_stack = Stack()
    my_stack.push('a')
    actual = my_stack.is_empty()
    expected = False
    assert actual == expected

def test_stack_push_multiple():
    my_stack = Stack()
    my_stack.push('a')
    my_stack.push('b')
    my_stack.push('c')
    actual = my_stack.top.value
    expected = 'c'
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

def test_stack_pop_multi():
    my_stack = Stack()
    my_stack.push('a')
    my_stack.push('b')
    my_stack.push('c')
    my_stack.pop()
    my_stack.pop()
    actual = my_stack.top.value
    expected = 'a'
    assert actual == expected

def test_stack_peek():
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    actual = my_stack.peek()
    expected = 2
    assert actual == expected

# ======== Queue ========

def test_queue_is_empty():
    my_queue = Queue()
    actual = my_queue.is_empty()
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
    my_queue.enqueue('d')
    actual = my_queue.dequeue()
    expected = 'a'
    assert actual == expected

def test_queue_peek():
    my_queue = Queue()
    my_queue.enqueue('a')
    my_queue.enqueue('b')
    actual = my_queue.peek()
    expected = 'a'
    assert actual == expected

# ======== PseudoQueue ========

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

def test_pseudo_dequeue():
    my_pseudo = PseudoQueue()
    my_pseudo.enqueue('a')
    my_pseudo.enqueue('b')
    my_pseudo.enqueue('c')
    actual = my_pseudo.dequeue()
    expected = 'a'
    assert actual == expected

# ======== AnimalShelter ========

def test_single_cat():
    shelter = AnimalShelter()
    cat = Cat()
    shelter.enqueue(cat)
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected

def test_single_dog():
    shelter = AnimalShelter()
    dog = Dog()
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected

def test_dog_preferred_with_cat_in_front():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(cat)
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected

def test_dog_then_cat():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected

def test_bad_pref():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("mouse")
    expected = None
    assert expected == actual
