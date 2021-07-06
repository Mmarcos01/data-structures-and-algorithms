class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Stack:

    def __init__(self, top = None):
        self.top = top

    def __str__(self):
        output = ''
        current_value = self.top
        while current_value:
            output += f'{ {current_value.value} } -> '
            current_value = current_value.next
        output += 'None'
        return output

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            current_node = self.top
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        return self

    def isEmpty(self):
      return self.top == None

    def pop(self):
            if self.isEmpty():
                raise Exception("Stack is empty!")
            self.top = self.top.next
            return self

