# Challenge Summary: Binary Tree and Binary Search Tree Implementation

### Feature Tasks

**Node**

Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

**Binary Tree**

1. Create a Binary Tree class.
1. Define a method for each of the depth first traversals, return an array of the values, ordered appropriately:
    - pre order
    - in order
    - post order

1. Raise/throw a custom, semantic error that describes what went wrong in calling any methods.

**Binary Search Tree**

1. Create a Binary Search Tree class.
    This class should be a sub-class of the Binary Tree Class, with the following additional methods:

    - Add
        - Arguments: value
        - Return: nothing
        - Adds a new node with that value in the correct location in the binary search tree.
    - Contains
        - Argument: value
        - Returns: boolean indicating whether or not the value is in the tree at least once.

---

### Structure and Testing

- Can successfully instantiate an empty tree
- Can successfully instantiate a tree with a single root node
- Can successfully add a left child and right child to a single root node
- Can successfully return a collection from a preorder traversal
- Can successfully return a collection from an inorder traversal
- Can successfully return a collection from a postorder traversal

---

# Challenge Summary: Find the Maximum Value in a Binary Tree

### Feature Tasks

Write the following method for the Binary Tree class:

**Find maximum value**
- Arguments: none
- Returns: number
    - Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard
![](tree-max.PNG)

## Collaborators

Kassie Bradshaw
Garfield Grant

---

# Challenge Summary: Breath First

### Feature Tasks
Write a function called breadth first that takes in an arguments of a tree.
The function will return a list of all values in the tree in the order they were encountered.

## Whiteboard
![](breadth_first.PNG)

## Collaborators

Garfield Grant
Kassie Bradshaw

---

# Challenge Summary: Fizz Buzz on a K-ary Tree

### Feature Tasks
Write a function called fizz-buzz-tree that takes in an argument of a k-ary tree.
The function will return a new k-ary tree. Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

- If the value is divisible by 3, replace the value with “Fizz”
- If the value is divisible by 5, replace the value with “Buzz”
- If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
- If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard
![](fizz_buzz_tree.PNG)

### Change Log

1.1: Completed Binary Tree method - 24 Jul 2021

1.2: Completed BST add and contains - 26 Jul 2021

1.3: Began BST max method - 26 Jul 2021

1.4: Breadth First - 29 Jul 2021

1.5: Began FizzBuzz on K-ary Tree - 02 Aug 2021
