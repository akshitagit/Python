"""
##Fix the Error: Mutating Arrays

Suppose I want to define a function that removes the last element of a list each time I call it, but does not mutate the original list. Fix the code so that the results are no longer mutating the list.
___
def minus_one(lst):
  arr.pop()
  return arr
_____



[Examples]

___
x = [1, 2, 3, 4, 5]
minus_one(x) ➞ [1, 2, 3, 4]  # 1st time function is called.
minus_one(x) ➞ [1, 2, 3]  # 2nd time function is called.
minus_one(x) ➞ [1, 2]  # 3rd time function is called.
minus_one(x) ➞ [1]  # 4th time function is called.

# What I want instead:
minus_one(x) ➞ [1, 2, 3, 4]  # 1st time function is called.
minus_one(x) ➞ [1, 2, 3, 4]  # 2nd time function is called.
minus_one(x) ➞ [1, 2, 3, 4]  # 3rd time function is called.
minus_one(x) ➞ [1, 2, 3, 4]  # 4th time function is called.
_____



[Notes]

N/A


[arrays] [bugs] 



-------------------------------------------------------------------
[Resources]
_________
Understanding Slice Notation
https://stackoverflow.com/questions/509211/understanding-slice-notation
I need a good explanation (references are a plus) on Python's slice notation. To me, this notation needs a bit of picking up. It looks extremely powerful, but I haven …
_________
_________
Python slice()
https://www.programiz.com/python-programming/methods/built-in/slice
Returns a slice object that can use used to slice strings, lists, tuple etc.
_________
_________
copy() Method
https://www.geeksforgeeks.org/python-list-copy-method/
Returns a shallow copy of a list. Shallow copy means that any modification in new list won’t be reflected to original list.
_________
_________
Shallow Copy and Deep Copy
https://www.programiz.com/python-programming/shallow-deep-copy
In this article, you’ll learn about shallow copy and deep copy in Python with the help of examples.
_________
""" 
# Your code should go here:

