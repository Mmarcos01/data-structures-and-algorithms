class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Stack:

    def __init__(self, top = None):
        self.top = top

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            raise Exception("No popping. Stack is empty!")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.isEmpty():
            raise Exception("No peeking. Stack is empty!")
        return self.top.value

class Queue:

    # def __init__(self, front = None):
        # self.front = front
        # self.rear = None
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False

    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty!")
        temp = self.front
        temp = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.isEmpty():
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
        if self.stack1.isEmpty():
            raise Exception("Can't dequeue. Stack is empty.")
        while not self.stack1.isEmpty():
            temp = self.stack1.pop()
            self.stack2.push(temp)
        removed = self.stack2.pop()
        while not self.stack2.isEmpty():
            popped = self.stack2.pop()
            self.stack1.push(popped)
        return removed
