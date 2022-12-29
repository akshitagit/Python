"""
####  Moving Partition  ####

Create a function to partition a list from left to right.


[Examples]

___
moving_partition([-1, -1, -1, -1])
➞ [[[-1], [-1, -1, -1]], [[-1, -1], [-1, -1]], [[-1, -1, -1], [-1]]]

moving_partition([1, 2, 3, 4, 5])
➞ [[[1], [2, 3, 4, 5]], [[1, 2], [3, 4, 5]], [[1, 2, 3], [4, 5]], [[1, 2, 3, 4], [5]]]

moving_partition([]) ➞ []
_____



[Notes]

___
*) With an n input, your output should be a list containing n-1 sublists. Each sublist should have two elements: the left and the right side of the partition (both should be non-empty, unless the input list is empty).
*) An empty list should return an empty list: []
___



[arrays] [higher_order_functions] 



-------------------------------------------------------------------
[Resources]
_________
How to Slice Lists and Tuples in Python
https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
A guide to slicing Python lists/arrays and Tuples, using multiple forms of syntax. We can use the short form of Python slicing, or the slice method.
_________

"""
#Your code should go here:

