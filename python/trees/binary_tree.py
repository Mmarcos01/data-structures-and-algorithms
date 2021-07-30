from stacks_queues.stacks_queues import Node, Queue

class Node:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def pre_order(self):
        # root >> left >> right
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

        current = self.root

        while current:
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                return True
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
        while not queue.isEmpty():
            front = queue.dequeue()
            list.append(front.value)

            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)
        return list
