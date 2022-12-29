"""
####  Sastry Numbers  ####

In this challenge, you have to establish if a given integer n is a Sastry number. If the number resulting from the concatenation of an integer n with its successor is a perfect square, then n is a Sastry Number.
Given a positive integer n, implement a function that returns True if n is a Sastry number, or False if it's not.


[Examples]

___
is_sastry(183) ➞ True
# Concatenation of n and its successor = 183184
# 183184 is a perfect square (428 ^ 2)

is_sastry(184) ➞ False
# Concatenation of n and its successor = 184185
# 184185 is not a perfect square

is_sastry(106755) ➞ True
# Concatenation of n and its successor = 106755106756
# 106755106756 is a perfect square (326734 ^ 2)
_____



[Notes]

___
*) A perfect square is a number with a square root equals to a whole integer.
*) You can expect only valid positive integers greater than 0 as input, without exceptions to handle. Zero is a perfect square, but the concatenation 00 isn't considered as a valid result to check.
___



[algorithms] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to check if a float value is a whole number?
https://stackoverflow.com/questions/21583758/how-to-check-if-a-float-value-is-a-whole-number
I am trying to find the largest cube root that is a whole number, that is less than 12,000. I am not sure how to check if it is a whole number or not though! I could co …
_________
_________
str() Method
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object.
_________
_________
Sastry-Numbers
https://www.geeksforgeeks.org/sastry-numbers/
A number N is a Sastry Number if N concatenated with N + 1 gives a perfect square.
_________
_________
How to find the division remainder of a number?
https://stackoverflow.com/questions/5584586/find-the-division-remainder-of-a-number
How could I go about finding the division remainder of a number in Python? For example: If the number is 26 and divided number is 7, then the division remainder is 5. ( …
_________
_________
How to Check If Given Number Is Perfect Square
https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
Given a number, check if it is perfect square or not.
_________
_________
endswith() Method
https://www.w3schools.com/python/ref_string_endswith.asp
Returns True if the string ends with the specified value, otherwise False.
_________
_________
sqrt() Method
https://www.geeksforgeeks.org/python-math-function-sqrt/
Returns the square root of any number.
_________

"""
#Your code should go here:

