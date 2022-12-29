"""
##Circle or Square

Given the radius of a circle and the area of a square,
return True if the circumference of the circle is greater than the square's perimeter
and False if the square's perimeter is greater than the circumference of the circle.


[Examples]

___
circle_or_square(16, 625) ➞ True

circle_or_square(5, 100) ➞ False

circle_or_square(8, 144) ➞ True
_____



[Notes]

___
*) You can use Pi to 2 decimal places (3.14).
*) Circumference of a circle equals 2 * Pi * radius.
*) To find the perimeter of a square using its area, find the square root of area (to get side length) and multiply that by 4.
___



[geometry] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Find the Square Root
https://www.programiz.com/python-programming/examples/square-root
In this program, you'll learn to find the square root of a number using exponent operator and cmath module.
_________
_________
Circle Formulas in Math
https://www.allmathtricks.com/circle-formulas-area-circumference/
Terminology and properties of circles in math | circle formulas like Area and circumference of the circle, Arc and sector of a circle, Segment of a circle.
_________
_________
How to Find Perimeter From Area
https://study.com/academy/lesson/how-to-find-perimeter-from-area.html
Here, you'll learn the steps to find the perimeter of a square, circle or rectangle from the area of the given shape. You'll also read about the units of measurement us …
_________
_________
How to Calculate Perimeter of a Square
https://byjus.com/maths/perimeter-of-square/
The perimeter of a square is defined as the length of the boundary of a square. Learn all the details of a perimeter of a square, its formula and derivation along with …
_________
""" 
# Your code should go here:

from math import pi
from math import sqrt
def circleSqaure(radius, sqArea):
    if (2 * round(pi, 2) * radius) > (sqrt(sqArea))*4:
        return True
    else:
        return False

print(circleSqaure(16, 625))
print(circleSqaure(5, 100))
print(circleSqaure(8 ,144))

# The program is complete.