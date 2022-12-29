"""
##Sum of Polygon Angles

Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).


[Examples]

___
sum_polygon(3) ➞ 180

sum_polygon(4) ➞ 360

sum_polygon(6) ➞ 720
_____



[Notes]

___
*) n will always be greater than 2.
*) The formula (n - 2) x 180 gives the sum of all the measures of the angles of an n-sided polygon.
___



[functional_programming] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Sum of Interior Angles of a Polygon
https://www.khanacademy.org/math/geometry-home/geometry-shapes/angles-with-polygons/v/sum-of-interior-angles-of-a-polygon#:~:text=s...%E2%80%9D-,(n%2D2)x%20180%20degrees%20%3A%20The%20formula%20for,of%20sides%20of%20the%20polygon%20.
The formula for finding the sum of all angles in a polygon.
_________
_________
Interior Angles of Polygons
https://www.mathsisfun.com/geometry/interior-angles-polygons.html
An Interior Angle is an angle inside a shape.
_________
_________
Regular Polygon
https://en.wikipedia.org/wiki/Regular_polygon
A polygon that is equiangular (all angles are equal in measure) and equilateral (all sides have the same length). Regular polygons may be either convex or star. In the …
_________
_________
How to convert a negative number to positive?
https://stackoverflow.com/questions/3854310/how-to-convert-a-negative-number-to-positive
How can I convert a negative number to positive in Python? (and keep a positive one)
_________
_________
Python Operators (+, -, /, *)
https://www.w3schools.com/python/python_operators.asp
The first paragraphs of this website explain the Python operators and their application in code. The most basic operators are +, -, /, and *.
_________
""" 
# Your code should go here:

def totalPolyAngle(sides):
    if sides <= 2:
        return "Please input n bigger than 2."
    else:
        return((sides-2) * 180)

print(totalPolyAngle(3))
print(totalPolyAngle(4))
print(totalPolyAngle(6))

# The program is complete.