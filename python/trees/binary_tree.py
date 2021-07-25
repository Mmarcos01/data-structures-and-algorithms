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
            if root.value:
                output.append(root.value)
            if root.left:
                pre_order_traversal(root.left)
            if root.right:
                pre_order_traversal(root.right)
            return
        pre_order_traversal(self.root)
        return output

    def in_order(self):
        # left >> root >> right
        output = []

        def in_order_traversal(root):
            if root.left:
                in_order_traversal(root.left)
            if root.value:
                output.append(root.value)
            if root.right:
                in_order_traversal(root.right)
            return
        in_order_traversal(self.root)
        return output

    def post_order(self):
        # left >> right >> root
        output = []

        def post_order_traversal(root):
            if root.left:
                post_order_traversal(root.left)
            if root.right:
                post_order_traversal(root.right)
            if root.value:
                output.append(root.value)
            return
        post_order_traversal(self.root)
        return output

class BinarySearchTree(BinaryTree):

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
