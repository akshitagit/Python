"""
##Minimal VII: Lambda Functions

Check the principles of minimalist code in the intro to the first challenge.
In the Code tab you will find a code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section below.
Write five adder functions:
___
*) add_2(x) should return 2 + x.
*) add_3(x) should return 3 + x.
*) add_5(x) should return 5 + x.
*) add_7(x) should return 7 + x.
*) add_11(x) should return 11 + x.
___



[Tips]

Functions that consist only of a return can be written as a one-liner with a lambda function.
For example, the code:
___
def are_same(a, b):
    return a == b
_____

Can be simplified to:
___
are_same = lambda a, b: a == b
_____



[Bonus]

lambda a, b: a == b is technically an anonymous function. However, it can be assigned to the identifier are_same and it can then be called using are_same().


[Notes]

___
*) This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your suggestions in the Comments.
*) Readability is indeed a subjective concept. Let's discuss it! Feel free to leave your opinion in the Comments.
*) You can find all the exercises in this series over here.
___



[closures] [higher_order_functions] [language_fundamentals] [logic] 



-------------------------------------------------------------------
[Resources]
_________
How to Use Python Lambda Functions
https://realpython.com/python-lambda/#closure
In this step-by-step tutorial, you'll learn about Python lambda functions. You'll see how they compare with regular functions and how you can use them in accordance wit …
_________
_________
Python Lambda
https://www.w3schools.com/python/python_lambda.asp
Say you have a function definition that takes one argument, and that argument  will be multiplied with an unknown number:
_________
_________
Python Closures
http://zetcode.com/python/python-closures/
This tutorial shows how to use closure functions in Python. Closures are nested functions that retain access to their outer scope.
_________
_________
exec() Method
https://www.programiz.com/python-programming/methods/built-in/exec
Executes the dynamically created program, which is either a string or a code object.
_________
_________
Lambda Expressions & Anonymous Functions
https://www.youtube.com/watch?v=25ovCm9jKfA
Also known as “anonymous functions”, allow you to create and use a function in a single line. They are useful when you need a short fu...
_________
""" 
# Your code should go here:

