"""
##Using the "and" Operator

Python has a logical operator and. The and operator takes two boolean values, and returns True if both values are True.
Consider a and b:
___
*) a is checked if it is True or False.
*) If a is False, False is returned.
*) b is checked if it is True or False.
*) If b is False, False is returned.
*) Otherwise, True is returned (as both a and b are therefore True ).
___

The and operator will only return True for True and True.
Make a function using the and operator.


[Examples]

___
And(True, False) ➞ False

And(True, True) ➞ True

And(False, True) ➞ False

And(False, False) ➞ False
_____



[Notes]

N/A


[language_fundamentals] [logic] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Python Operators
https://www.programiz.com/python-programming/operators
In this article, you'll learn everything about different types of operators in Python, their syntax and how to use them with examples.
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Operators are used to perform operations on variables and values. In the example below, we use the + operator to add together two values.
_________
_________
Python Operators: Arithmetic, Comparison, Logical and More
https://www.programiz.com/python-programming/operators
In this tutorial, you'll learn everything about different types of operators in Python, their syntax, and how to use them with examples.
_________
""" 
# Your code should go here:

def And(bool1, bool2):
    if bool1 == True and bool2 == True:
        return True
    else:
        return False

print(And(True, False))
print(And(True, True))
print(And(False, True))
print(And(False, False))

# The program is complete.