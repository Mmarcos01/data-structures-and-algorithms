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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def insertAfter(self, value, new_value):
        current = self.head
        while current.next:
            if value == current.value:
                break
            current = current.next
        if current is None:
            print("none found")
        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node

    def insertBefore(self, value, new_value):
        current = self.head
        while current.next:
            if value == current.next.value:
                break
            current = current.next
        if current is None:
            print("none found")
        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node
