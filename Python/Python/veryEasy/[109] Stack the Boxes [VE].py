"""
##Stack the Boxes

Here's an image of four models. Some of the cubes are hidden behind other cubes.
Model one consists of one cube. Model two consists of four cubes, and so on...

Write a function that takes a number n and returns the number of stacked boxes in a model n levels high, visible and invisible.


[Examples]

___
stack_boxes(1) ➞ 1

stack_boxes(2) ➞ 4

stack_boxes(0) ➞ 0
_____



[Notes]

Step n is a positive integer.


[algebra] [algorithms] [logic] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Arithmetic operators are used with numeric values to perform common mathematical operations, such as addition, subtraction, multiplication, division, modulus, exponenti …
_________
_________
How To Do Math in Python 3 with Operators
https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators
Numbers are extremely common in programming. They are used to represent things like screen size dimensions, geographic locations, money and points, the amount of time t …
_________
""" 
# Your code should go here:

def stackBoxes(n):
    if n >= 0:
        return n ** 2
    else:
        return "Step n can only be a positive integer."

print(stackBoxes(1))
print(stackBoxes(2))
print(stackBoxes(0))
print(stackBoxes(10))
print(stackBoxes(-10))

# The program is complete.