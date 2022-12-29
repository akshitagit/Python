"""
####  Greater Than the Sum?  ####

For each number in a list, check if that number is greater than the sum of all numbers that appear before it in the list. If all numbers in the list pass this test, return True. Return False otherwise.


[Examples]

___
greater_than_sum([2, 3, 7, 13, 28]) ➞ True

# 3 > 2 = True
# 7 > 2 + 3 = True
# 13 > 2 + 3 + 7 = True
# 28 > 2 + 3 + 7 + 13 = True

greater_than_sum([1, 2, 4, 6, 13]) ➞ False

# 2 > 1 = True
# 4 > 1 + 2 = True
# 6 > 1 + 2 + 4 = False
# 13 > 1 + 2 + 4 + 6 = False
_____



[Notes]

The first number in any list will always pass the test.


[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
enumerate() Function
https://www.programiz.com/python-programming/methods/built-in/enumerate
Adds counter to an iterable and returns it (the enumerate object).
_________
_________
Data Structures
https://docs.python.org/3/tutorial/datastructures.html
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.in …
_________
_________
Using Python Lists
http://openbookproject.net/thinkcs/python/english3e/lists.html
A list is an ordered collection of values. The values that make up a list are called its elements, or its items. We will use the term element or item to mean the same t …
_________

"""
#Your code should go here:

