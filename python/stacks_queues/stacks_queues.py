class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Stack:

    def __init__(self, top = None):
        self.top = top

    def push(self, value):
        self.top = Node(value, self.top)

    def is_empty(self):
        '''Return true if self.top is None, else return false'''
        return self.top == None

    def pop(self):
        if self.is_empty():
            raise Exception("No popping. Stack is empty!")
        temp = self.top
        self.top = self.top.next
        return temp.value

    def peek(self):
        if self.is_empty():
            raise Exception("No peeking. Stack is empty!")
        return self.top.value

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        '''Return true if self.top is None, else return false'''
        return self.front == None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        temp = self.front
        self.front = temp.next
        return temp.value

    def peek(self):
        if self.is_empty():
            raise Exception("No Peeking. Queue is empty!")
        return self.front.value

class PseudoQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    # check the top, if exists, take the value and push it into stack 2
    def dequeue(self):
        if self.stack1.is_empty():
            raise Exception("Can't dequeue. Stack is empty.")
        while not self.stack1.is_empty():
            temp = self.stack1.pop()
            self.stack2.push(temp)
        removed = self.stack2.pop()
        while not self.stack2.is_empty():
            temp = self.stack2.pop()
            self.stack1.push(temp)
        return removed

class AnimalShelter:
    def __init__(self):
        self.shelter = Queue()

    def enqueue(self, animal):
        self.shelter.enqueue(animal)

    def dequeue(self, pref):
        if not pref in ["dog", "cat"]:
            return None
        current = self.shelter.dequeue()
        while current:
            if self._is_preferred(pref, current):
                    return current
            self.shelter.enqueue(current)
            current = self.shelter.dequeue()
        return current

    def _is_preferred(self, pref, animal):
        if pref == "cat":
            class_type = Cat
        elif pref == "dog":
            class_type = Dog

        return isinstance(animal, class_type)

class Dog:
    def __repr__(self):
        return "I am a Dog instance"


class Cat:
    def __repr__(self):
        return "I am a Cat instance"
