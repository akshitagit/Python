"""
##Nothing is Nothing?

Given any number of parameters (which is signified using *args syntax), return True if none of the variables are falsy/empty.


[Examples]

___
nothing_is_nothing(0, False, [], {}) ➞ False

nothing_is_nothing(33, "Hello", (True, True, 3)) ➞ True

nothing_is_nothing(True, None) ➞ False
_____



[Notes]

___
*) *args allows a function to take any number of parameters.
*) Falsy refers to values which evaluate to False in a boolean context. This includes (but is not limited to) variables such as 0, False, None, empty sets, lists and tuples.
___



[data_structures] [language_fundamentals] [validation] 



-------------------------------------------------------------------
[Resources]
_________
all() Method
https://www.w3schools.com/python/ref_func_all.asp
Returns True if all items in an iterable are true, otherwise it returns False.
_________
_________
How to call a function with argument list in Python?
https://stackoverflow.com/questions/817087/call-a-function-with-argument-list-in-python
I'm trying to call a function inside another function in python, but can't find the right syntax. In this case first call will work, and second won't. What I want to mo …
_________
""" 
# Your code should go here:

