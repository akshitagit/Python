"""
##I'd Like a New Shade of Blue, Please

I have a bucket containing an amount of navy blue paint and I'd like to paint as many walls as possible. Create a function that returns the number of complete walls that I can paint, before I need to head to the shops to buy more.
___
*) n is the number of square meters I can paint.
*) w and h are the widths and heights of a single wall in meters.
___



[Examples]

___
how_many_walls(100, 4, 5) ➞ 5

how_many_walls(10, 15, 12) ➞ 0

how_many_walls(41, 3, 6) ➞ 2
_____



[Notes]

___
*) Don't count a wall if I don't manage to finish painting all of it before I run out of paint.
*) All walls will have the same dimensions.
*) All numbers will be positive integers.
___



[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
What does floor division ('//') in Python do?
https://www.quora.com/What-does-floor-division-in-Python-do
Returns the integral part of the quotient.
_________
_________
Beginner Python Area of a Room
https://stackoverflow.com/questions/41786365/beginner-python-area-of-a-room
Right now I am working on a program to calculate the area of a room in order to purchase cans of paint. I am just a three weeks into my class and I'm a little overwhelm …
_________
_________
Estimating How Much Paint to Buy
https://www.dummies.com/home-garden/home-painting/estimating-how-much-paint-to-buy/
To estimate the amount of paint you need in order to cover the walls of a room, add together the length of all the walls and then multiply the number by the height of t …
_________
_________
floor() and ceil() Function
https://www.geeksforgeeks.org/floor-ceil-function-python/?ref=gcse
The floor() method in Python returns the floor of x i.e., the largest integer not greater than x. The method ceil(x) in Python returns a ceiling value of x i.e., the sm …
_________
_________
Area of Rectangles Review
https://www.khanacademy.org/math/cc-third-grade-math/imp-geometry/imp-multiply-to-find-area/a/area-rectangles-review
Area is the space inside of a two-dimensional shape. We can also think of area as the amount of space a shape covers. For example, the rectangle below has an area of 12 …
_________
""" 
# Your code should go here:
from math import floor as flr

""" Method 1 """
# def wallCanPaint(sqmtr, widths, heights):
#     return flr(sqmtr/(widths * heights))

""" Method 2 """
wallCanPaint = lambda sqmtr, widths, heights : flr(sqmtr/(widths * heights)) if sqmtr > 0 and widths > 0 and heights > 0 else "Please input positive value."

print(wallCanPaint(100, 4, 5))
print(wallCanPaint(10,15, 12))
print(wallCanPaint(41, 3, 6))
print(wallCanPaint(0, 1, 2))

# The program is complete.