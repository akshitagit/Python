"""
####  Right Shift by Division  ####

The right shift operation is similar to floor division by powers of two.
Sample calculation using the right shift operator ( >> ):
___
80 >> 3 = floor(80/2^3) = floor(80/8) = 10
-24 >> 2 = floor(-24/2^2) = floor(-24/4) = -6
-5 >> 1 = floor(-5/2^1) = floor(-5/2) = -3
_____

Write a function that mimics (without the use of >>) the right shift operator and returns the result from the two given integers.


[Examples]

___
shift_to_right(80, 3) ➞ 10

shift_to_right(-24, 2) ➞ -6

shift_to_right(-5, 1) ➞ -3

shift_to_right(4666, 6) ➞ 72

shift_to_right(3777, 6) ➞ 59

shift_to_right(-512, 10) ➞ -1
_____



[Notes]

___
*) There will be no negative values for the second parameter y.
*) This challenge is more like recreating of the right shift operation, thus, the use of the operator directly is prohibited.
*) Alternatively, you can solve this challenge via recursion.
*) A recursive version of this challenge can be found via this link.
___



[bit_operations] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Floor Division
https://python-reference.readthedocs.io/en/latest/docs/operators/floor_division.html
Also referred to as integer division. The resultant value is a whole integer, though the result’s type is not necessarily int.
_________
_________
How To Do Math with Operators
https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators
This tutorial will go over operators that can be used with number data types in Python.
_________
_________
Operators
https://jakevdp.github.io/WhirlwindTourOfPython/04-semantics-operators.html
Python implements seven basic binary arithmetic operators, two of which can double as unary operators. They are summarized in the following table...
_________
_________
Bitwise Operators
https://www.geeksforgeeks.org/python-bitwise-operators/
Used to perform bitwise calculations on integers. The integers are first converted into binary and then operations are performed on bit by bit, hence the name bitwise o …
_________

"""
#Your code should go here:

