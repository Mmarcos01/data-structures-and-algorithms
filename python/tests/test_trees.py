import pytest
from trees.binary_tree import KaryTree, Node, BinaryTree, BinarySearchTree, KaryTree

# @pytest.mark.skip("pending")
def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"

def test_node_has_left_of_none():
    node = Node("apple")
    assert node.left is None

def test_node_has_right_of_none():
    node = Node("apple")
    assert node.right is None

def test_create_binary_tree():
    tree = BinaryTree()
    assert tree

def test_binary_tree_has_root():
    tree = BinaryTree()
    assert tree.root is None

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

def test_bst_add_multiple():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    actual = tree.pre_order()
    assert tree.root.value == 1
    assert actual == [1, 2, 3]

def test_contains_true():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    actual = tree.contains(3)
    assert actual == True

def test_contains_false():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(2)
    tree.add(4)
    actual = tree.contains(3)
    assert actual == False

def test_find_max():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(2)
    tree.add(4)
    actual = tree.max()
    assert actual == 4

def test_find_max_2():
    tree = BinarySearchTree()
    tree.add(346)
    tree.add(34)
    tree.add(7532)
    tree.add(65)
    tree.add(57)
    actual = tree.max()
    assert actual == 7532

def test_find_max_empty():
    tree = BinarySearchTree()
    actual = tree.max()
    assert actual ==  "Empty Tree"

def test_breadth_first():
    tree = BinarySearchTree()
    tree.root = Node(3)
    tree.root.left = Node(2)
    tree.root.right = Node(11)
    tree.root.left.left = Node(1)
    tree.root.right.right = Node(8)
    actual = tree.breadth_first()
    assert actual == [3, 2, 11, 1, 8]

def test_negative(negative_tree):
    actual = negative_tree.breadth_first()
    assert actual == [-2, -7, -5, -2, -9]

def test_kary_tree_fizzbuzz():
    tree = KaryTree()
    tree.root = Node(3)
    tree.children[0] = Node(5)
    tree.children[1] = Node(6)
    tree.children[2] = Node(15)
    actual = tree.fizz_buzz_tree()
    assert actual.root == Node('Fizz')

@pytest.fixture
def negative_tree():
    tree = BinarySearchTree()
    tree.root = Node(-2)
    tree.root.left = Node(-7)
    tree.root.right = Node(-5)
    tree.root.left.left = Node(-2)
    tree.root.right.right = Node(-9)
    return tree
