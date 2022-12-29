"""
##Basketball Points

You are counting points for a basketball game, given the amount of 3-pointers scored and 2-pointers scored, find the final points for the team and return that value ([2 -pointers scored, 3-pointers scored]).


[Examples]

___
points(1, 1) ➞ 5

points(7, 5) ➞ 29

points(38, 8) ➞ 100
_____



[Notes]

N/A


[language_fundamentals] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Python Operators: Arithmetic, Comparison, Logical and more.
https://www.programiz.com/python-programming/operators
In this tutorial, you'll learn everything about different types of operators in Python, their syntax and how to use them with examples.
_________
_________
What does the Star operator mean in Python?
https://www.tutorialspoint.com/What-does-the-Star-operator-mean-in-Python
Is used in Python with more than one meaning attached to it.For numeric data types, * is used as multiplication operator>>> a=10;b= ...
_________
""" 
# Your code should go here:

def basketBallPoints(pointer2, pointer3):
    return ((pointer2 * 2) + (pointer3 * 3))

print(basketBallPoints(1, 1))
print(basketBallPoints(7,5))
print(basketBallPoints(38, 8))

# This program is complete.