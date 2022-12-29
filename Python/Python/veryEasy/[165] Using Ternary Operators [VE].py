"""
##Using Ternary Operators

The ternary operator (sometimes called Conditional Expressions) in Python is an alternative to the if... else... statement.
It is written in the format:
___
result_if_true if condition else result_if_false
_____

Ternary operators are often more compact than multi-line if statements, and are useful for simple conditional tests.
For example:
___
is_nice = True

# Using ternary operator.
state = "nice" if is_nice else "not nice"

# Equivalent code using multi-line if statements.
if is_nice:
    state = "nice"
else:
    state = "not nice"
_____

Write a function that uses the ternary operator to return "yeah" if b is True, and "nope" otherwise.


[Examples]

___
yeah_nope(True) ➞ "yeah"

yeah_nope(False) ➞ "nope"
_____



[Notes]

N/A


[conditions] [language_fundamentals] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Ternary Operator in Python
https://www.geeksforgeeks.org/ternary-operator-in-python/
Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It simply allows to test a condi …
_________
_________
Conditional Expressions
https://docs.python.org/3/reference/expressions.html#613conditionalexpressions
This chapter explains the meaning of the elements of expressions in Python.
_________
_________
Ternary Operators
https://book.pythontips.com/en/latest/ternary_operators.html
Ternary operators are more commonly known as conditional expressions in Python. These operators evaluate something based on a condition being true or not. They became a …
_________
_________
Ternary Operator
https://syntaxdb.com/ref/python/ternary
Is used to return a value based on the result of a binary condition.
_________
""" 
# Your code should go here:

