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

    def __init__(self):
        self.root = None

    def add(value):
        new_node = Node(value)
        current = value.root
        node = None

        while current:
            node = current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        if node ==  None:
            node = new_node

    def contains(value):
        pass
