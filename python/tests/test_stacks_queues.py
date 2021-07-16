import pytest
from stacks_queues.stacks_queues import Node, Stack, Queue, PseudoQueue, AnimalShelter

def test_instantiate_empty_node():
    node1 = Node(1)
    assert node1.value == 1
    assert node1.next == None

# ======== Stack ========

def test_stack_isEmpty():
    my_stack = Stack()
    actual = my_stack.isEmpty()
    expected = True
    assert actual == expected

def test_stack_push_multiple():
    my_stack = Stack()
    my_stack.push('a')
    my_stack.push('b')
    actual = my_stack.top.next.value
    expected = 'a'
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

def test_empty_animal_shelter():
    new_shelter = AnimalShelter()
    assert new_shelter.front == None
    assert new_shelter.rear == None
    assert new_shelter.length == 0

def test_animal_enqueue():
    new_shelter = AnimalShelter()
    input1 = {"animal": "dog"}
    input2 = {"animal": "cat"}
    new_shelter.enqueue(input1)
    new_shelter.enqueue(input2)
    assert new_shelter.rear.value["animal"] == "cat"

def test_dequeue_pref_in_front():
    new_shelter = AnimalShelter()
    input1 = {"animal": "dog"}
    input2 = {"animal": "cat"}
    new_shelter.enqueue(input1)
    new_shelter.enqueue(input2)
    actual = new_shelter.dequeue("dog")
    expected = "dog"
    assert actual == expected

def test_dequeue_pref_in_middle():
    new_shelter = AnimalShelter()
    input1 = {"animal": "dog"}
    input2 = {"animal": "cat"}
    input3 = {"animal": "dog"}
    new_shelter.enqueue(input1)
    new_shelter.enqueue(input2)
    new_shelter.enqueue(input3)
    actual = new_shelter.dequeue("cat")
    expected = "cat"
    assert actual == expected

def test_dequeue_pref_at_end():
    new_shelter = AnimalShelter()
    input1 = {"animal": "dog"}
    input2 = {"animal": "dog"}
    input3 = {"animal": "cat"}
    new_shelter.enqueue(input1)
    new_shelter.enqueue(input2)
    new_shelter.enqueue(input3)
    actual = new_shelter.dequeue("cat")
    expected = "cat"
    assert actual == expected

# ======== Validate Brackets ========



# ======== Pytest Fixtures ========

def test_dequeue_on_empty_queue_raises_exception():
    empty_shelter = AnimalShelter()
    with pytest.raises(Exception):
        empty_shelter.dequeue("dog")


def test_dequeue_with_pref_animal_not_in_shelter(all_dogs):
    actual = all_dogs.dequeue("cat")
    expected = None
    assert actual == expected
    assert all_dogs.length == 5

@pytest.fixture
def new_shelter():
    new_shelter = AnimalShelter()
    input1 = {"animal": "dog"}
    input2 = {"animal": "dog"}
    input3 = {"animal": "cat"}
    input4 = {"animal": "dog"}
    input5 = {"animal": "cat"}
    new_shelter.enqueue(input1)
    new_shelter.enqueue(input2)
    new_shelter.enqueue(input3)
    new_shelter.enqueue(input4)
    new_shelter.enqueue(input5)
    return new_shelter


@pytest.fixture
def all_dogs():
    all_dogs = AnimalShelter()
    input1 = {"animal": "dog"}
    input2 = {"animal": "dog"}
    input3 = {"animal": "dog"}
    input4 = {"animal": "dog"}
    input5 = {"animal": "dog"}
    all_dogs.enqueue(input1)
    all_dogs.enqueue(input2)
    all_dogs.enqueue(input3)
    all_dogs.enqueue(input4)
    all_dogs.enqueue(input5)
    return all_dogs


@pytest.fixture
def cat_last():
    cat_last = AnimalShelter()
    input1 = {"animal": "dog"}
    input2 = {"animal": "dog"}
    input3 = {"animal": "dog"}
    input4 = {"animal": "dog"}
    input5 = {"animal": "cat"}
    cat_last.enqueue(input1)
    cat_last.enqueue(input2)
    cat_last.enqueue(input3)
    cat_last.enqueue(input4)
    cat_last.enqueue(input5)
    return cat_last
