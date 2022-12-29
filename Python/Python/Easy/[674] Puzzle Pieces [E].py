"""
####  Puzzle Pieces  ####

Write a function that takes two lists and adds the first element in the first list with the first element in the second list, the second element in the first list with the second element in the second list, etc, etc. Return True if all element combinations add up to the same number. Otherwise, return False.


[Examples]

___
puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True
# 1 + 4 = 5;  2 + 3 = 5;  3 + 2 = 5;  4 + 1 = 5
# Both lists sum to [5, 5, 5, 5]

puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]) ➞ True

puzzle_pieces([1, 2], [-1, -1]) ➞ False

puzzle_pieces([9, 8, 7], [7, 8, 9, 10]) ➞ False
_____



[Notes]

___
*) Each list will have at least one element.
*) Return False if both lists are of different length.
___



[arrays] [higher_order_functions] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Python | Check if all elements in a List are same
https://www.geeksforgeeks.org/python-check-if-all-elements-in-a-list-are-same/
Given a list, write a Python program to check if all the elements in given list are same.
_________
_________
zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
Creates an iterator that will aggregate elements from two or more iterables. You can use the resulting iterator to quickly and consistently solve common programming pro …
_________
_________
map() Method
https://www.programiz.com/python-programming/methods/built-in/map
Applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
_________
_________
Functional Interface to Built-in Operators
https://pymotw.com/3/operator/index.html
Programming using iterators occasionally requires creating small functions for simple expressions. Sometimes, these can be implemented as lambda functions, but for some …
_________
_________
How to Add Two Lists Element-Wise in Python
https://www.kite.com/python/answers/how-to-add-two-lists-element-wise-in-python
Adding two lists of equal lengths element-wise results in a list where each element is the sum of the corresponding elements in the original lists. For instance, [1, 2, …
_________

"""
#Your code should go here:

