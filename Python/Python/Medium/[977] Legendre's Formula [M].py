"""
####  Legendre's Formula  ####

Legendre's formula finds the exponent of the largest power of some prime p that divides (is a factor of) the factorial of some number n.
Legendre's formula example (p = 2 and n = 27):

So 2^23 is the largest power of 2 that divides 27!.
The formula returns the sum of many fractions (rounded down) with n as the numerator and a steadily increasing power of p as the denominator, stopping when it exceeds the numerator.
To illustrate:
___
p = 5
n = 100

int(100/5) + int(100/25)
# No 100/125 because 125 > 100.
_____

___
p = 2
n = 128

int(128/2) + int(128/4) + int(128/8) + ... + int(128/128)
_____

Given p and n, return the result of Legendre's formula (see Resources).


[Examples]

___
legendre(5, 100) ➞ 24

legendre(2, 128) ➞ 127

legendre(3, 50) ➞ 22
_____



[Notes]

___
*) p and n will be positive integers.
*) When p exceeds n, the result should be 0.
___



[algebra] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
Floor Based Division
https://www.askpython.com/python/python-floor-based-division
The // operator in Python 3 is used to perform floor-based division.
_________
_________
Legendre's Formula
https://en.wikipedia.org/wiki/Legendre%27s_formula
In mathematics, Legendre's formula gives an expression for the exponent of the largest power of a prime p that divides the factorial n!.
_________
_________
Legendre’s Formula
https://www.geeksforgeeks.org/legendres-formula-highest-power-of-prime-number-that-divides-n/
Given an integer n and a prime number p, find the largest x such that px (p raised to power x) divides n! (factorial).
_________

"""
#Your code should go here:

