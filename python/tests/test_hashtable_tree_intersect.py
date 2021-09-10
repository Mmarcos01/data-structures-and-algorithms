import pytest
from hashtables.hashtable_tree_intersect import hash_tree_intersection
from trees.binary_tree import BinaryTree, Node


def test_proof_of_life():
    assert hash_tree_intersection

def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"

def test_node_has_left_of_none():
    node = Node("apple")
    assert node.left is None

def test_node_has_right_of_none():
    node = Node("apple")
    assert node.right is None

def test_binary_tree_has_root():
    tree = BinaryTree()
    assert tree.root is None

def test_create_binary_tree():
    tree = BinaryTree()
    assert tree

def test_hashtable_tree_intersect(tree1, tree2):
    actual = hash_tree_intersection(tree1, tree2)
    expected = [2,5,9]
    assert actual == expected

def test_no_duplicates(tree1, tree3):
    actual = hash_tree_intersection(tree1,tree3)
    expected = []
    assert actual == expected

@pytest.fixture
def tree1():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(6)
    tree.root.right.right = Node(9)
    return tree

@pytest.fixture
def tree2():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(1)
    tree.root.right = Node(5)
    tree.root.left.left = Node(8)
    tree.root.right.right = Node(9)
    return tree

@pytest.fixture
def tree3():
    tree = BinaryTree()
    tree.root = Node(21)
    tree.root.left = Node(11)
    tree.root.right = Node(51)
    tree.root.left.left = Node(81)
    tree.root.right.right = Node(91)
    return tree
