class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Stack:

    def __init__(self, top = None):
        self.top = top

    def __str__(self):
        output = ''
        while self.top:
            output += f'{ {self.top.value} } -> '
            self.top = self.top.next
        output += 'None'
        return output

    # def print_stack(self):
    #     if self.top is None:
    #         print("Empty Stack!")
    #     else:
    #         node = self.top
    #         while node is not None:
    #             print(node.value)
    #             node = node.next

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

    def __init__(self, front = None):
        self.front = front
        # self.rear = None

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
