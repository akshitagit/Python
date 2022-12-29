"""
##Return Negative

Create a function that takes a number as an argument and returns negative of that number. Return negative numbers without any change.


[Examples]

___
return_negative(4) ➞ -4

return_negative(15) ➞ -15

return_negative(-4) ➞ -4

return_negative(0) ➞ 0
_____



[Notes]

N/A


[language_fundamentals] [logic] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
abs() Method
https://www.programiz.com/python-programming/methods/built-in/abs
Returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Operators are used to perform operations on variables and values.
_________
_________
Python Conditions and If Statements
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics. These conditions can be used in several ways, most commonly in "if statements" and loops. An "if stateme …
_________
_________
Ternary Operator in Python
https://www.tutorialspoint.com/ternary-operator-in-python
Many programming languages support ternary operator, which basically define a conditional expression.Similarly the ternary operator in python is used to return ...
_________
""" 
# Your code should go here:

def conv2Neg(num1):
    if num1 >= 0:
        return (num1 * (-1))
    else:
        return num1

print(conv2Neg(4))
print(conv2Neg(15))
print(conv2Neg(-4))
print(conv2Neg(0))
print(conv2Neg(-11))

# The program is complete.