"""
####  Spin Around, Touch the Ground  ####

Given a list of directions to spin, "left" or "right", return an integer of how many full 360° rotations were made. Note that each word in the list counts as a 90° rotation in that direction.


[Worked Example]

___
spin_around(["right", "right", "right", "right", "left", "right"]) ➞ 1
# You spun right 4 times (90 * 4 = 360)
# You spun left once (360 - 90 = 270)
# But you spun right once more to make a full rotation (270 + 90 = 360)
_____



[Examples]

___
spin_around(["left", "right", "left", "right"]) ➞ 0

spin_around(["right", "right", "right", "right", "right", "right", "right", "right"]) ➞ 2

spin_around(["left", "left", "left", "left"]) ➞ 1
_____



[Notes]

___
*) Return a positive number.
*) All tests will only include the words "right" and "left".
___



[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
abs() Method
https://www.programiz.com/python-programming/methods/built-in/abs
Returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.
_________
_________
Calculate Radial Angle in Both Directions Given Pixel Coordinates
https://stackoverflow.com/questions/37259366/using-python-to-calculate-radial-angle-in-clockwise-counterclockwise-directions
You can simplify your code quite a bit by using a couple of simple rules. Simple code is less likely to have bugs. First, converting between clockwise and counter-cloc …
_________

"""
#Your code should go here:

