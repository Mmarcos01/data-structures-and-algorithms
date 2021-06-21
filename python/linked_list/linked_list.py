class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, head = None):
        self.head = head
        # initialization here
        # pass

    def insert(self, any_value):
        node = Node(any_value)

        if self.head is not None:
            node.next == self.head
        self.head == node

    def includes(self, value):

        current_value = self.head

        while current_value != None:
            if current_value.head == value:
                return True
            current_value = current_value.next
        return False
