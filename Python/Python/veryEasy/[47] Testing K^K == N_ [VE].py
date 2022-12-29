"""
##Testing K^K == N?

Write a function that returns True if k^k == n for input (n, k) and return False otherwise.


[Examples]

___
k_to_k(4, 2) ➞ True

k_to_k(387420489, 9) ➞ True
# 9^9 == 387420489

k_to_k(3124, 5) ➞ False

k_to_k(17, 3) ➞ False
_____



[Notes]

The ^ operator refers to exponentiation operation **, not the bitwise XOR operation.


[bit_operations] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to Do Math in Python with Operators
https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators
This tutorial will go over operators that can be used with number data types in Python. An operator is a symbol or function that indicates an operation. For example, in …
_________
_________
Floating Point Numbers
https://www.youtube.com/watch?v=PZRI1IfStY0
Why can't floating point do money? It's a brilliant solution for speed of calculations in the computer, but how and why does moving the decimal point (well, in this cas …
_________
_________
Exponentiation (**)
https://www.w3schools.com/python/python_operators.asp
Arithmetic operators are used with numeric values to perform common mathematical operations.
_________
_________
math.pow() Method
https://www.w3schools.com/python/ref_math_pow.asp
Returns the value of x raised to power y.
_________
_________
Python Bitwise Operators with Syntax and Examples
https://data-flair.training/blogs/python-bitwise-operators/
In this tutorial, we discuss Python Bitwise AND, OR, XOR, Left-shift, Right-shift, and 1’s complement Bitwise Operators in Python Programming. Along with this, we will …
_________
""" 
# Your code should go here:

def kExpoEqN(n ,k):
    if ((k ** k) == n):
        return True
    else:
        return False

print(kExpoEqN(4,2))
print(kExpoEqN(387420489, 9))
print(kExpoEqN(17, 3))
print(kExpoEqN(3124, 5))

# The program is complete.