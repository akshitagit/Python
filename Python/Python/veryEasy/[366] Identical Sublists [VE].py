"""
##Identical Sublists

Create a function that takes in a two-dimensional list and returns the number of sub-lists with only identical elements.


[Examples]

___
count_identical([
  [1],
  [2],
  [3],
  [4]
]) ➞ 4

# Single-item lists still count as having identical elements.


count_identical([
  [1, 2],
  [2, 3],
  [3, 4],
  [4, 4]
]) ➞ 1


count_identical([
  [33, 33],
  [5],
  ["a", "a"],
  [2, 2, 2],
  [1, 2, 2],
  [3, 1]
]) ➞ 4

# 4 lists with identical elements: [33, 33], [5], ["a", "a"], and [2, 2, 2]


count_identical([
  ["@", "@", "@", "@"],
  [2, 3], [3, 4], [4, 4]
]) ➞ 2
_____



[Notes]

Single-element lists count as (trivially) having identical elements.


[arrays] [conditions] [loops] 



-------------------------------------------------------------------
[Resources]
_________
set() Constructor
https://www.programiz.com/python-programming/methods/built-in/set
Constructs a Python set from the given iterable and returns it.
_________
_________
len() Method
https://www.w3schools.com/python/ref_func_len.asp
Returns the number of items in an object.
_________
_________
sum() Method
https://www.w3schools.com/python/ref_func_sum.asp
Returns a number, the sum of all items in an iterable.
_________
""" 
# Your code should go here:

