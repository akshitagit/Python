"""
##Triangle and Parallelogram Area Finder

Write a function that accepts base (decimal), height (decimal) and shape ("triangle", "parallelogram") as input and calculates the area of that shape.


[Examples]

___
area_shape(2, 3, "triangle") ➞ 3

area_shape(8, 6, "parallelogram") ➞ 48

area_shape(2.9, 1.3, "parallelogram") ➞ 3.77
_____



[Notes]

___
*) Area of a triangle is 0.5 * b * h
*) Area of a parallelogram is b * h
*) Assume triangle and parallelogram are the only inputs for shape.
___



[algorithms] [conditions] [geometry] [math] 



-------------------------------------------------------------------
[Resources]
_________
Area of Plane Shapes
https://www.mathsisfun.com/area.html
Area of Plane Shapes
_________
_________
If/Else
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics: Equals: a == b Not Equals: a != b Less than: a < b Less than or equal to: a <= b Greater than: a > b Gre …
_________
""" 
# Your code should go here:

shapeArea = lambda base, height, shape : base * height if shape.lower() == "parallelogram" else 0.5 * base * height if shape.lower() == "triangle" else "Please input shapes from the given only."

# def shapeArea(base, height, shape):
#     if shape.lower() == "parallelogram":
#         return base * height
#     elif shape.lower() == "triangle"
#         return 0.5 * base * height
#     else:
#         return "Please input shapes from the given only."

print(shapeArea(2, 3, "triangle"))
print(shapeArea(8, 6, "parallelogram"))
print(shapeArea(2.9, 1.3, "parallelogram"))
print(shapeArea(2, 3, "Nitkarsh"))

# The program is complete.