"""
####  Function Factory  ####

Create a function that takes a "base number" as an argument. This function should return another function which takes a new argument, and returns the sum of the "base number" and the new argument.
Please check the examples below for a clearer representation of the behavior expected.


[Examples]

___
# Calling make_plus_function(5) returns a new function that takes an input,
# and returns the result when adding 5 to it.

plus_five = make_plus_function(5)

plus_five(2) ➞ 7

plus_five(-8) ➞ -3
_____

___
# Calling make_plus_function(10) returns a new function that takes an input,
# and returns the result when adding 10 to it.

plus_ten = make_plus_function(10)

plus_ten(0) ➞ 10

plus_ten(188) ➞ 198

plus_five(plus_ten(0)) ➞ 15
_____



[Notes]

All inputs will be valid numbers.


[closures] [functional_programming] [higher_order_functions] 



-------------------------------------------------------------------
[Resources]
_________
How to Use Python Lambda Functions
https://realpython.com/python-lambda/
Python and other languages like Java, C#, and even C++ have had lambda functions added to their syntax, whereas languages like LISP or the ML family of languages, Haske …
_________
_________
Python Closures
https://www.programiz.com/python-programming/closure
In this article, you'll learn what is a Python closure, how to define a closure, and reasons why you should use it. Before getting into what a closure is, we have to fi …
_________

"""
#Your code should go here:

