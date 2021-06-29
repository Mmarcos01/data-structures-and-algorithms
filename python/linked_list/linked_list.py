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
        return self

    def insertAfter(self, value, new_value):
        current = self.head
        while current.next:
            if value == current.value:
                break
            current = current.next
     # if current is None: # if there is no head print message
 #     print("none found")
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


def zipLists(list1, list2):
    current_1 = list1.head
    current_2 = list2.head
    while current_1 and current_2:
        list_1_next = current_1.next
        list_2_next = current_2.next
        current_1.next = current_2
        current_2.next = list_1_next
        current_1 = list_1_next
        current_2 = list_2_next
    list2.head = current_2
    return list1


