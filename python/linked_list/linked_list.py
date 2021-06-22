class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    """
    create a linked list, ability to insert new nodes and check for existing nodes
    """

    def __init__(self, head = None):
        self.head = head

    def __str__(self):
        output = ''
        current_value = self.head
        while current_value:
            output += f'{ {current_value.value} } -> '
            #walk/traverse
            current_value = current_value.next
        output += 'None'
        return output

    def insert(self, any_value):
        self.head = Node(any_value, self.head)

    def includes(self, value):

        current_value = self.head

        while current_value:
            if current_value.value == value:
                return True
            current_value = current_value.next
        return False
