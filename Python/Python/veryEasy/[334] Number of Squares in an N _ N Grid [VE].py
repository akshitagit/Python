"""
##Number of Squares in an N * N Grid

Create a function that calculates the number of different squares in an n * n square grid. Check the Resources tab.


[Examples]

___
number_squares(2) ➞ 5

number_squares(4) ➞ 30

number_squares(5) ➞ 55
_____



[Explanation]

___
*) If n = 0 then the number of squares is 0
*) If n = 1 then the number of squares is 1 + 0 = 1
*) If n = 2 then the number of squares is 2^2 + 1 = 4 + 1 = 5
*) If n = 3 then the number of squares is 3^2 + 5 = 9 + 5 = 14
___

As you can see, for each value of n the number of squares is n squared + the number of squares from the previous value of n.


[Notes]

___
*) Input is a positive integer.
*) Square pyramidal number.
___



[math] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Square Pyramidal Number in Python
https://tutorialspoint.dev/algorithm/mathematical-algorithms/square-pyramidal-number-sum-squares
A Square pyramidal number represents sum of squares of first natural numbers. First few Square pyramidal numbers are 1, 5, 14, 30, 55, 91, 140, 204, 285, 385, 5
_________
_________
round() Function
https://www.w3schools.com/python/ref_func_round.asp
Returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
_________
_________
Square Pyramidal Number
https://en.wikipedia.org/wiki/Square_pyramidal_number
A figurate number that represents the number of stacked spheres in a pyramid with a square base. Square pyramidal numbers also solve the problem of counting the number …
_________
_________
Basic Operators
https://www.tutorialspoint.com/python/python_basic_operators.htm
Are the constructs which can manipulate the value of operands.
_________
_________
Square Pyramidal Number Formula
https://math.wikia.org/wiki/Square_pyramidal_number
Uses pictures and descriptions to explain how a square pyramidal number works. (represents a pyramid with a base and four sides.)
_________
""" 
# Your code should go here:

