"""
##Find the Perimeter of a Rectangle

Create a function that takes length and width and finds the perimeter of a rectangle.


[Examples]

___
find_perimeter(6, 7) ➞ 26

find_perimeter(20, 10) ➞ 60

find_perimeter(2, 9) ➞ 22
_____



[Notes]

___
*) Don't forget to return the result.
*) If you're stuck, find help in the Resources tab.
*) If you're really stuck, find solutions in the Solutions tab.
___



[geometry] [language_fundamentals] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How to find the perimeter of a rectangle?
https://www.mathopenref.com/rectangleperimeter.html
Like any polygon, the perimeter is the total distance around the outside, which can be found by adding together the length of each side. I the case of a rectangle, oppo …
_________
_________
How to Find the Perimeter of a Rectangle
https://www.varsitytutors.com/basic_geometry-help/how-to-find-the-perimeter-of-a-rectangle
The perimeter of a rectangle is found by adding up the length of all four sides. Since the two long sides are 12 cm, and the two shorter sides are 7 cm the perimeter ca …
_________
_________
Perimeter of a Rectangle Formula
https://byjus.com/maths/perimeter-of-rectangle/
The perimeter of a rectangle is defined as the sum of all the sides of a rectangle. For any polygon, the perimeter formulas are the total distance around its sides. In …
_________
_________
Rectangle
https://en.wikipedia.org/wiki/Rectangle
A quadrilateral with four right angles. It can also be defined as an equiangular quadrilateral, since equiangular means that all of its angles are equal (360°/4 = 90°). …
_________
_________
What is Perimeter of a Rectangle?
https://www.splashlearn.com/math-vocabulary/geometry/perimeter-of-a-rectangle
Definition of Perimeter of a Rectangle explained with real life illustrated examples. Also learn the facts to easily understand math glossary with fun math worksheet.
_________
_________
Video Walk Through
https://www.youtube.com/watch?v=zp8D_6NVVPE
In this video, you will learn how to solve these problems in Python: 0:11 Equality of 3 Values, 2:34 Temperature Conversion, 4:43 Find the Perimeter of a Rectangle.
_________
""" 
# Your code should go here:

def rectPeriFind(length, breadth):
    return ((length * 2) + (breadth * 2))

print(rectPeriFind(6,7))
print(rectPeriFind(20, 10))
print(rectPeriFind(2,9))
print(rectPeriFind(3,3))

# The program is complete.