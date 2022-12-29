"""
##Area of a Triangle

Write a function that takes the base and height of a triangle and return its area.


[Examples]

___
tri_area(3, 2) ➞ 3

tri_area(7, 4) ➞ 14

tri_area(10, 10) ➞ 50
_____



[Notes]

___
*) The area of a triangle is: (base * height) / 2
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[geometry] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Area of a Triangle
https://www.youtube.com/watch?v=xz6gBA0M9FY
Students learn the formula for the area of a triangle, and are asked to solve problems using this formula. Note that right triangle formulas and trigonometry are used e …
_________
_________
Area of Triangles
https://www.mathsisfun.com/algebra/trig-area-triangle-without-right-angle.html
When we know two sides and the included angle (SAS), there is another formula (in fact three equivalent formulas) we can use.
_________
_________
Area of a Triangle
https://www.mathgoodies.com/lessons/vol1/area_triangle
The area of a polygon is the number of square units inside that polygon. Area is 2-dimensional like a carpet or an area rug. A triangle is a three-sided polygon. We wil …
_________
_________
Python Area of Triangle
https://www.javatpoint.com/python-area-of-triangle
Area of a triangle = (s*(s-a)*(s-b)*(s-c))-1/2 Here s is the semi-perimeter and a, b and c are three sides of the triangle.
_________
_________
4 Ways to Calculate the Area of a Triangle
https://www.wikihow.com/Calculate-the-Area-of-a-Triangle#:~:text=You%20can%20find%20the%20area,divided%20by%202%20equals%204.
The most common way to find the area of a triangle is to take half of the base times the height. Numerous other formulas exist, however, for finding the area of a trian …
_________
""" 
# Your code should go here:

def triArea(height, base):
    return ((base * height)/2)

print(int(triArea(3,2)))
print(int(triArea(7,4)))
print(int(triArea(10,10)))

# This program is complete.