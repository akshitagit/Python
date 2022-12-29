"""
##Area of a Rectangle

Create a function that calculates the area of a rectangle. If the arguments are invalid, your function must return -1.


[Examples]

___
area(3, 4) ➞ 12

area(10, 11) ➞ 110

area(-1, 5) ➞ -1

area(0, 2) ➞ -1
_____



[Notes]

N/A


[algebra] [geometry] [math] 



-------------------------------------------------------------------
[Resources]
_________
Area of a Rectangle
https://www.tutorialgateway.org/python-program-to-find-area-of-a-rectangle/
Perimeter is the distance around the edges. We can calculate perimeter of a rectangle using below formula Perimeter = 2 * (Width + Height).
_________
_________
Ternary Operator
https://www.geeksforgeeks.org/ternary-operator-in-python/#:~:text=Ternary%20operators%20also%20known%20as,else%20making%20the%20code%20compact.
Are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. It simply allows to test a condition in a single …
_________
_________
How to write a program in python 3.3.4 that works out the area of a rectangle?
https://stackoverflow.com/questions/21880810/how-to-write-a-program-in-python-3-3-4-that-works-out-the-area-of-a-rectangle
How do you write a program that works out the area of a rectangle, by collecting the height and width of the rectangle from the user input, calculates the area and disp …
_________
_________
Operators
https://www.programiz.com/python-programming/operators
In this tutorial, you'll learn everything about different types of operators in Python, their syntax and how to use them with examples.
_________
_________
Calculating Area
https://www.skillsyouneed.com/num/area.html
Learn how to calculate the area of common shapes for real life situations. We provide plain English explanations and working examples to help you learn.
_________
""" 
# Your code should go here:

rectArea = lambda length, breadth : length * breadth if length > 0 and breadth > 0 else -1

print(rectArea(3, 4))
print(rectArea(10, 11))
print(rectArea(-1, 5))
print(rectArea(0, 2))

# The program is complete.