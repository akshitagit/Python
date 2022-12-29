"""
##Radians to Degrees

Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.


[Examples]

___
radians_to_degrees(1) ➞ 57.3

radians_to_degrees(20) ➞ 1145.9

radians_to_degrees(50) ➞ 2864.8
_____



[Notes]

The number π can be loaded from the math module with from math import pi.


[logic] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
round() Method
https://www.w3schools.com/python/ref_func_round.asp
Returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
_________
_________
Converting Radians to Degrees
https://www.youtube.com/watch?v=z0-1gBy1ykE
Worked example showing how to convert radians to degrees. Practice this lesson yourself.
_________
_________
Radian to Degrees Converter
https://www.rapidtables.com/convert/number/how-radians-to-degrees.html
A guide from the website Rapid Tables showing how to convert a value in radians to a value in degrees
_________
_________
Converting Radians to Degrees and Degrees to Radians
https://www.mathwarehouse.com/trigonometry/radians/convert-degee-to-radians.php
How to convert radians to degrees and back lesson explained with interactive applet, pictures and several practice problems.
_________
_________
How to Convert Radians to Degrees
https://stackoverflow.com/questions/9875964/how-can-i-convert-radians-to-degrees-with-python
Radians and degrees are two separate units of measure that help people express and communicate precise changes in direction. Wikipedia has some great intuition with the …
_________
"""

# Your code should go here:

from math import pi
def radToDeg(radians):
    return round((radians * (180/pi)),1)

print(radToDeg(1))
print(radToDeg(20))
print(radToDeg(50))

# The program is complete.