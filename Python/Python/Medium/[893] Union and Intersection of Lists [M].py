"""
####  Union and Intersection of Lists  ####

Create a function that takes in two lists and returns an intersection list and a union list.

While the input lists may have duplicate numbers, the returned intersection and union lists should be set-ified - that is, contain no duplicates. Returned lists should be sorted in ascending order.
___
List 1: [5, 6, 6, 6, 8, 9]
List 2: [3, 3, 4, 4, 5, 5, 8]

Intersection: [5, 8]
# 5 and 8 are the only 2 numbers that exist in both lists.

Union: [3, 4, 5, 6, 8, 9]
# Each number exists in at least one list.
_____



[Examples]

___
intersection_union([1, 2, 3, 4, 4], [4, 5, 9]) ➞ [[4], [1, 2, 3, 4, 5, 9]]

intersection_union([1, 2, 3], [4, 5, 6]) ➞ [[], [1, 2, 3, 4, 5, 6]]

intersection_union([1, 1], [1, 1, 1, 1]) ➞ [[1], [1]]
_____



[Notes]

___
*) Order of output should be: [Intersection], [Union].
*) Remember both output lists should be in ascending order.
*) Each input list will have at least one element.
*) If both lists are disjoint (share nothing in common), return an empty list [] for the intersection.
___



[arrays] [functional_programming] 



-------------------------------------------------------------------
[Resources]
_________
union() Method
https://www.programiz.com/python-programming/methods/set/union
Returns a new set with distinct elements from all the sets.
_________
_________
list() Constructor
https://www.programiz.com/python-programming/methods/built-in/list
Creates a list in Python.
_________
_________
intersection() Set
https://www.programiz.com/python-programming/methods/set/intersection
Returns a new set with elements that are common to all sets.
_________
_________
Sorted() Method
https://www.programiz.com/python-programming/methods/built-in/sorted
Learn about the Python sorted() method with the help of examples.
_________

"""
#Your code should go here:

