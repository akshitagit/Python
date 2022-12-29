"""
##Left Shift by Powers of Two

The left shift operation is similar to multiplication by powers of two.
Sample calculation using the left shift operator (<<):
___
10 << 3 = 10 * 2^3 = 10 * 8 = 80
-32 << 2 = -32 * 2^2 = -32 * 4 = -128
5 << 2 = 5 * 2^2 = 5 * 4 = 20
_____

Write a function that mimics (without the use of <<) the left shift operator and returns the result from the two given integers.


[Examples]

___
shift_to_left(5, 2) ➞ 20

shift_to_left(10, 3) ➞ 80

shift_to_left(-32, 2) ➞ -128

shift_to_left(-6, 5) ➞ -192

shift_to_left(12, 4) ➞ 192

shift_to_left(46, 6) ➞ 2944
_____



[Notes]

___
*) There will be no negative values for the second parameter y.
*) This challenge is more like recreating of the left shift operation, thus, the use of the operator directly is prohibited.
*) Alternatively, you can solve this challenge via recursion.
*) A recursive version of this challenge can be found via this link.
___



[bit_operations] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How to square a number in Python?
https://kodify.net/python/math/square/#:~:text=Python%20has%20three%20ways%20to,*%20)%20a%20value%20with%20itself.
The square of a number is that number multiplied by itself. But what are the ways to do that in the Python programming language? Let's find out.
_________
""" 
# Your code should go here:

