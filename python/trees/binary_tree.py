from stacks_queues.stacks_queues import Node, Queue

class Node:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

class KaryNode:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

class BinaryTree:

    def __init__(self):
        self.root = None

    def pre_order(self):
        # root >> left >> right
        if self.root == None:
            return "Tree is empty."
        output = []

        def pre_order_traversal(root):
            if root:
                output.append(root.value)
                pre_order_traversal(root.left)
                pre_order_traversal(root.right)
        pre_order_traversal(self.root)
        return output

    def in_order(self):
        # left >> root >> right
        output = []

        def in_order_traversal(root):
            if root:
                in_order_traversal(root.left)
                output.append(root.value)
                in_order_traversal(root.right)
        in_order_traversal(self.root)
        return output

    def post_order(self):
        # left >> right >> root
        output = []

        def post_order_traversal(root):
            if root:
                post_order_traversal(root.left)
                post_order_traversal(root.right)
                output.append(root.value)
        post_order_traversal(self.root)
        return output

    def breadth_first_traversal(input_tree):
        if input_tree.root == None:
            return "Tree is empty."
        queue = Queue()
        queue.enqueue(input_tree.root)
        result = []
        while not queue.is_empty():
            front = queue.dequeue()
            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)
            result.append(front.value)
        return result

    def find_max_using_order_function(self):

        if self.root is None:
            return "Tree is empty"

        value_list = self.pre_order()
        max_val = value_list[0]

        for i in value_list:
            if i > max_val:
                max_val = i

        return max_val

class BinarySearchTree(BinaryTree):

    def add(self, value):
        new_node = Node(value)
        current = self.root

        if current is None:
            self.root = new_node

        while current:
            if value > current.value:
                if current.right is None:
                    current.right = new_node
                    return self
                current = current.right

            else:
                if current.left is None:
                    current.left = new_node
                    return self
                current = current.left

    def contains(self, value):
        if self.root is None:
            return None

        current = self.root
        while current:
            if current.value == value:
                return True
            if value > current.value:
                current = current.right
            else:
                current = current.left

        return False

    def max(self):
        if self.root is None:
            return "Empty Tree"
        values = self.pre_order()
        max_val = values[0]
        for i in values:
            if i > max_val:
             max_val = i
        return max_val

    def breadth_first(self):
        if self.root is None:
            return 'Empty Tree!'
        list = []
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            front = queue.dequeue()
            list.append(front.value)

            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)
        return list

class KaryTree:

    def __init__(self, node = None):
        self.root = node

    def kary_breadth_first(self):
        queue = Queue()
        queue.enqueue(self.root)
        result = []
        while not queue.is_empty():
            front = queue.dequeue()
            for node in front.children:
                queue.enqueue(node)
            result.append(front.value)
        return result

def fizz_buzz_conditions(value):
    if value % 15 == 0:
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    else:
        return str(value)


def fizz_buzz_tree(tree):
    if tree.root is None:
        raise Exception("Tree is empty")
    queue = Queue()
    queue.enqueue(tree.root)
    while not queue.is_empty():
        front = queue.dequeue()
        front.value = fizz_buzz_conditions(front.value)
        for node in front.children:
            queue.enqueue(node)

    return tree
