"""
##Return the Sum of Two Numbers

Create a function that takes two numbers as arguments and returns their sum.


[Examples]

___
addition(3, 2) ➞ 5

addition(-3, -6) ➞ -9

addition(7, 3) ➞ 10
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[algebra] [language_fundamentals] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Numeric Types — int, float, complex
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
There are three distinct numeric types: integers, floating point numbers, and complex numbers. In addition, Booleans are a subtype of integers. Integers have unlimited …
_________
_________
Chapter 3: Functions
https://automatetheboringstuff.com/chapter3/
You’re already familiar with the print(), input(), and len() functions from the previous chapters. Python provides several builtin functions like these, but you can als …
_________
_________
How to Do Math in Python 3 with Operators
https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators
Numbers are extremely common in programming. They are used to represent things like screen size dimensions, geographic locations, money and points, the amount of time t …
_________
_________
Math Operator
https://www.w3schools.com/python/python_howto_add_two_numbers.asp
Using the math operator called "+" or addition to add numbers together.
_________
_________
Basic Operators
https://www.tutorialspoint.com/python/python_basic_operators.htm
Are the constructs which can manipulate the value of operands. Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.
_________
_________
Program to Add Two Numbers
https://www.thecrazyprogrammer.com/2017/04/python-program-add-two-numbers.html
Here you will get python program to add two numbers. The program will first ask user to enter two numbers, calculate their sum and finally print it. input() is an inbui …
_________
_________
Operators
https://www.w3schools.com/python/python_operators.asp
Are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
_________
""" 
# Your code should go here:

def addition(int1, int2):
    return int1 + int2

print(addition(3,2))
print(addition(-3,-6))
print(addition(7, 3))

# The program is complete.