"""
##Omnipresent Value

A value is omnipresent if it exists in every sublist inside the main list.
To illustrate:
___
[[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
# 3 exists in every element inside this list, so is omnipresent.
_____

Create a function that determines whether an input value is omnipresent for a given list.


[Examples]

___
is_omnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ True

is_omnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ False

is_omnipresent([[5], [5], [5], [6, 5]], 5) ➞ True

is_omnipresent([[5], [5], [5], [6, 5]], 6) ➞ False
_____



[Notes]

Sub-lists can be any length.


[algorithms] [arrays] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Check if Element Exists in List of Lists
https://www.geeksforgeeks.org/python-check-if-element-exists-in-list-of-lists/
Given a list of lists, the task is to determine whether the given element exists in any sublist or not. Given below are a few methods to solve the given task.
_________
_________
all() Method
https://www.programiz.com/python-programming/methods/built-in/all
Returns True when all elements in the given iterable are true. If not, it returns False.
_________
_________
Comprehensions in Python
https://www.geeksforgeeks.org/comprehensions-in-python/
Comprehensions provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined.
_________
""" 
# Your code should go here:

