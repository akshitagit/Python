"""
####  Circular Shift  ####

Write a function that takes two lists (lst1 and lst2) and an int n, and returns True if the second list equals the first list shifted by n positions. Otherwise, return False.


[Examples]

___
circular_shift([1, 2, 3, 4], [3, 4, 1, 2], 2) ➞ True

circular_shift([1, 1], [1, 1], 6) ➞ True

circular_shift([0, 1, 2, 3, 4, 5], [3, 4, 5, 2, 1, 0], 3) ➞ False
_____



[Notes]

___
*) The two lists will have the same length.
*) n can be a negative value.
___



[arrays] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Efficient way to rotate a list in Python?
https://stackoverflow.com/questions/2150108/efficient-way-to-rotate-a-list-in-python
What is the most efficient way to rotate a list in python?
_________
_________
How to Shift Elements in a List in Python
https://kite.com/python/answers/how-to-shift-elements-in-a-list-in-python
Shifting a list rotates its elements. Elements moved off the end are rotated to the beginning. For example, shifting [1, 2, 3, 4 ,5] twice to the right results in [4, 5 …
_________
_________
Example of Circular Shifts
https://www.youtube.com/watch?v=F9SYSmJpSs4
This video is part of the Udacity course "Software Architecture & Design".
_________
_________
zip(*iterables)
https://docs.python.org/3.3/library/functions.html#zip
Make an iterator that aggregates elements from each of the iterables. Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the arg …
_________
_________
insert() Method
https://www.programiz.com/python-programming/methods/list/insert
Inserts an element to the list at the specified index.
_________
_________
pop() Method
https://www.programiz.com/python-programming/methods/list/pop
Removes the item at the given index from the list and returns the removed item.
_________
_________
Shift or Rotate an Array
https://www.delftstack.com/howto/python/python-shift-array/
This tutorial demonstrates how to shift or rotate an array in Python.
_________

"""
#Your code should go here:

