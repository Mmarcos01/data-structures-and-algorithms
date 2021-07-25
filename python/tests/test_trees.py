import pytest
from trees.binary_tree import Node, BinaryTree, BinarySearchTree

# @pytest.mark.skip("pending")
def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"


# @pytest.mark.skip("pending")
def test_node_has_left_of_none():
    node = Node("apple")
    assert node.left is None


# @pytest.mark.skip("pending")
def test_node_has_right_of_none():
    node = Node("apple")
    assert node.right is None


# @pytest.mark.skip("pending")
def test_create_binary_tree():
    tree = BinaryTree()
    assert tree


# @pytest.mark.skip("pending")
def test_binary_tree_has_root():
    tree = BinaryTree()
    assert tree.root is None


# @pytest.mark.skip("pending")
def test_create_binary_search_tree():
    tree = BinarySearchTree()
    assert tree

def test_pre_order_add_left_and_right():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.right = Node(3)
    tree.root.left = Node(4)
    actual = tree.pre_order()
    assert actual == [1, 4, 3]

def test_in_order_add_left_and_right():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    actual = tree.in_order()
    assert actual == [4, 2, 5, 1, 3]

def test_post_order_add_left_and_right():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    actual = tree.post_order()
    assert actual == [4, 5, 2, 3, 1]

def test_bst_add():
    tree = BinarySearchTree()
    # tree.root.left = Node(2)
    # tree.root.right = Node(3)
    # insert = BinarySearchTree(tree)
    # insert.add(4)
    actual =  tree.add(1)
    assert actual == 1
