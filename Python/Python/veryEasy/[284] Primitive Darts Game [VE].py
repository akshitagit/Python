"""
##Primitive Darts Game

Darts is a target game played by throwing feathered darts at a circular board with numbered spaces. Our darts game is the simplest of all games. The score of a single turn is calculated based on the distance from the middle. You need to create a function that takes the dart location as two cartesian coordinates (x, y) and returns a score based on the distance from the middle, aka Bullseye (x=0, y=0).
___
*) Bullseye and inner circle scores = 10 points
*) Middle ring scores = 5 points
*) Outer ring scores = 1 point
*) Outside the target = 0 points
___

We play it simple so a dart in the double or treble ring counts as usual and does not affect the segment score.
Board and circle radius is as follows:
___
*) Board radius and outer circle radius = 10 units
*) Middle circle radius = 5 units
*) Inner circle radius = 1 unit
___



[Short Description]

Convert cartesian coordinates (x, y) to polar coordinates (R, phi) and return the score based on the R value. R > 10 gives 0 points, 10 >= R > 5 gives 1 point, 5 >= R > 1 gives 5 points, R <= 1 gives 10 points.


[Examples]

___
darts_scoring(0, 0) ➞ 10

darts_scoring(3, 2) ➞ 5

darts_scoring(0, -0.8) ➞ 10
_____



[Notes]

___
*) X, Y values can be both positive and negative.
*) X, Y values can be int and float.
*) No wrong type values will be given.
___



[conditions] [control_flow] [language_fundamentals] [math] 



-------------------------------------------------------------------
[Resources]
_________
Distance Between 2 Points
https://www.mathsisfun.com/algebra/distance-2-points.html
When we know the horizontal and vertical distances between two points we can calculate the straight line distance like this ...
_________
_________
How to Calculate Square Root in Python
https://www.pythonpool.com/square-root-in-python/
In layman language square root can be defined as A square root of a number is a value that, when multiplied by itself, gives the number. In Python or any other Programm …
_________
_________
Polar and Cartesian Coordinates
https://www.mathsisfun.com/polar-cartesian-coordinates.html
When we know a point in Cartesian Coordinates (x,y) and we want it in Polar Coordinates (r,θ) we solve a right triangle with two known sides.
_________
_________
If Statement
https://www.educba.com/if-statement-in-python/
Guide to If Statement in Python. Here we discuss syntax, flowchart, comparison along with different examples and code implementation.
_________
""" 
# Your code should go here:

