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
        current_value = self.head
        output = ''
        while current_value:
            output += f'{ {current_value.value} } -> '
            current_value = current_value.next
        return output + 'None'

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
        return self

    def insertAfter(self, value, new_value):
        current = self.head
        while current.next:
            if value == current.value:
                break
            current = current.next
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

    def kth_from_the_end(self, k):
        if k < 0:
            return "K is negative"
        if self.head is None:
            return None

        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next
        if count < k:
            raise Exception ('k is larger than link list')
        current = self.head
        count = count - k

        while count > 1:
            current = current.next
            count -= 1

        return current.value

def zipLists(ll1, ll2):
    curr1 = ll1.head
    curr2 = ll2.head
    while curr1 and curr2:
        temp1 = curr1.next
        temp2 = curr2.next
        curr1.next = curr2
        curr2.next = temp1
        curr1 = temp1
        curr2 = temp2
    return ll1

