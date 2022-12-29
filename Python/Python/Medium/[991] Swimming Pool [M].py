"""
####  Swimming Pool  ####

Suppose a swimming pool blueprint can be represented as a 2D list, where 1s represent the pool and 0s represent the rest of the backyard.
___
[[0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]
# Legitimate
_____

Suppose a pool is considered legitimate if it does not touch any of the four borders in this 2D list.
___
[[1, 1, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]
# Illegitimate! 
# The 1s are touching both the left "fence" and the upper "fence".
_____

Create a function that returns True if the pool plan is legitimate, and False otherwise.


[Examples]

___
is_legitimate([
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0]
]) ➞ True

is_legitimate([
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 0, 0],
  [0, 0, 1, 1, 1, 0, 0, 0]
]) ➞ False

is_legitimate([
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0]
]) ➞ True
_____



[Notes]

N/A


[arrays] [higher_order_functions] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Indexing and Slicing for Lists, Tuples, Strings
https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
List is arguably the most useful and ubiquitous type in Python. One of the reasons it’s so handy is Python slice notation. In short, slicing is a flexible tool to build …
_________
_________
zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
Creates an iterator that will aggregate elements from two or more iterables. You can use the resulting iterator to quickly and consistently solve common programming pro …
_________
_________
How to Sum Elements of Two Lists
https://therenegadecoder.com/code/how-to-sum-elements-of-two-lists-in-python/
In short, one of the best ways to sum elements of two lists in Python is to use a list comprehension in conjunction with the addition operator. For example, we could pe …
_________

"""
#Your code should go here:

