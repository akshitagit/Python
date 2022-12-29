"""
####  Accumulating Product  ####

Create a function that takes a list and returns a list of the accumulating product.


[Examples]

___
accumulating_product([1, 2, 3, 4]) ➞ [1, 2, 6, 24]
# [1, 2, 6, 24] can be written as [1, 1 x 2, 1 x 2 x 3, 1 x 2 x 3 x 4]

accumulating_product([1, 5, 7]) ➞ [1, 5, 35]

accumulating_product([1, 0, 1, 0]) ➞ [1, 0, 0, 0]

accumulating_product([]) ➞ []
_____



[Notes]

An empty list should return an empty list [].


[arrays] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
reduce() Method
https://www.geeksforgeeks.org/reduce-in-python/
Used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. This function is defined in “functools” m …
_________
_________
Python Itertools.accumulate()
https://www.geeksforgeeks.org/python-itertools-accumulate/
Is a collection of tools for handling iterators.
_________
_________
How to Calculate a Cumulative Product of a List Using List Comprehension
https://stackoverflow.com/questions/62239593/how-to-calculate-a-cumulative-product-of-a-list-using-list-comprehension/62239675
Problem is given an input_list = [1, 2, 3, 4, 5] return a list with each element as multiple of all elements till that index starting from left to right.
_________
_________
numpy.cumprod() Function
https://www.geeksforgeeks.org/numpy-cumprod-in-python/
Is used when we want to compute the cumulative product of array elements over a given axis.
_________

"""
#Your code should go here:

