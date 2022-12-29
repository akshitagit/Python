"""
##Divides Evenly

Given two integers, a and b, return True if a can be divided evenly by b. Return False otherwise.


[Examples]

___
divides_evenly(98, 7) ➞ True
# 98/7 = 14

divides_evenly(85, 4) ➞ False
# 85/4 = 21.25
_____



[Notes]

a will always be greater than or equal to b.


[math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Check Whether a Number Is Divisible by Another Number
https://www.w3resource.com/python-exercises/python-basic-exercise-147.php
Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user.
_________
_________
Modulo Operator (%)
https://realpython.com/python-modulo-operator/
Returns the remainder of dividing two numbers.
_________
_________
Operators and Operands
https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/OperatorsandOperands.html
Operators are special tokens that represent computations like addition, multiplication and division. The values the operator works on are called operands.
_________
_________
Lambda and Filter in Python (Examples)
https://www.geeksforgeeks.org/lambda-filter-python-examples/
We can use Lambda function inside the filter() built-in function to find all the numbers divisible by 13 in the list. In Python, anonymous function means that a functio …
_________
_________
Python Program to Check if a Number is Odd or Even
https://www.programiz.com/python-programming/examples/odd-even
Source code to check whether a number entered by user is either odd or even in Python programming with output and explanation…
_________
""" 
# Your code should go here:

def evenDiv(a, b):
    if a >= b:
        if (a % b == 0):
            return True
        else:
            return False
    else:
        return "Please input 'a' bigger or equal to 'b'."

print(evenDiv(98, 7))
print(evenDiv(85, 4))
print(evenDiv(99, 9))
print(evenDiv(9, 9))
print(evenDiv(9, 10))

# The program is complete.