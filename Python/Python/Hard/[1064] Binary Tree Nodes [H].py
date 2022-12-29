"""
####  Binary Tree Nodes  ####

We have two lists _N and _P, where _N represents the value of a node in Binary Tree, and _P is the parent of _N.

Write a function to find the node type of the node within this Binary Tree, ordered by the value of the node. Output one of the following:
___
*) Root: If node is root node.
*) Leaf: If node is leaf node.
*) Inner: If node is neither root nor leaf node.
*) Not exist: If node not exist.
___

___
node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 5) ➞ "Root"

node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 6) ➞ "Leaf"

node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 2) ➞ "Inner"

node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 10) ➞ "Not exist"
_____




[Notes]

All values of _N list are unique.


[algorithms] [arrays] [conditions] [interview] 



-------------------------------------------------------------------
[Resources]
_________
Binary Tree Data Structure
https://www.geeksforgeeks.org/binary-tree-data-structure/
A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and …
_________

"""
#Your code should go here:

