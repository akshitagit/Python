"""
####  Bound Sort  ####

Create a function that returns True if an input array can be completely sorted by only sorting within the bounds [0, n] (inclusive), where n is smaller than or equal to the array's length, and False otherwise.


[Examples]

___
bound_sort([1, 6, 5, 3, 8, 9], [0, 3]) ➞ True
# If [1, 6, 5, 3] is sorted to [1, 3, 5, 6], the array is completely sorted.

bound_sort([1, 6, 5, 3, 8, 9], [0, 2]) ➞ False
# Even if [1, 6, 5] is sorted to [1, 5, 6], the array is still not completely sorted.

bound_sort([1, 9, 2, 5, 7], [0, 4]) ➞ True

bound_sort([1, 9, 2, 5, 7], [0, 3]) ➞ False
# Sorting from [0, 3] gives us [1, 2, 5, 9, 7], array still not completely sorted.
_____



[Notes]

___
*) Numbers in array will be unique.
*) The lower index of the bound will always be 0.
___



[arrays] [sorting] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to slice a list, string, tuple
https://note.nkmk.me/en/python-slice-usage/
How to slice a list, string, tuple. In Python, a slice (slicing) represented by colons (eg: [2:5:2]) allows you to select items in a sequence object, such as a list, st …
_________
_________
sorted() Function
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________

"""
#Your code should go here:

