"""
##Using Lambda Functions

Create a function that returns its given argument, but by using a lambda function.
A lambda function is constructed like so:
___
lambda_func=lambda ***parameters***:#code here
_____



[Examples]

___
lambda_func(3) ➞ 3

lambda_func("3") ➞ "3"

lambda_func(True) ➞ True
_____



[Notes]

Check the Resources tab for more information on lambda functions.


[data_structures] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Python Lambda Functions
https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
In Python, an anonymous function means that a function is without a name. As we already know that the def keyword is used to define a normal function in Python. Similar …
_________
_________
Lambda Functions
https://www.w3schools.com/python/python_lambda.asp
We can use lambda functions for a shorter version of normal functions.
_________
_________
Python Lambda Functions
https://www.guru99.com/python-lambda-function.html
A Lambda Function in Python programming is an anonymous function or a function having no name. It is a small and restricted function having no more than one line. Just …
_________
"""
# Your code should go here:

lamdaFunction = lambda a : a

print(lamdaFunction(9))
print(lamdaFunction("Hey!"))
print(lamdaFunction(True))

# The program is complete.