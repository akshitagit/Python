"""
##Solving Exponential Equations With Logarithms

Create a function that takes a number a and finds the missing exponent x so that a when raised to the power of x is equal to b.


[Examples]

___
solve_for_exp(4, 1024) ➞ 5

solve_for_exp(2, 1024) ➞ 10

solve_for_exp(9, 3486784401) ➞ 10
_____



[Notes]

a is raised to the power of what in order to equal b?


[algorithms] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Log Functions in Python
https://www.geeksforgeeks.org/log-functions-python/
Python offers many inbuild logarithmic functions under the module “math” which allows us to compute logs using a single line. There are 4 variants of logarithmic functi …
_________
_________
Natural Logarithm in Python
https://python-forum.io/Thread-Natural-Logarithm-in-Python
I need to input an equation, but I need help with expressing the Natural Logarithm in Python. The equation is: (7.35 x E) + [17.34 x ln(Len)] + [4.96 x ln(Conc)] + [0.8 …
_________
_________
Solving Exponential Equations with Logarithms
https://www.purplemath.com/modules/solvexpo2.htm
Demonstrates how to solve exponential equations by using logarithms. Explains how to recognize when logarithms are necessary. Provides worked examples showing how to ob …
_________
_________
The Change-of-Base Formula
https://www.purplemath.com/modules/logrules5.htm
You may have noticed that your calculator only has keys for figuring the values for the common (that is, the base-10) log and the natural (that is, the base-e) log. The …
_________
""" 
# Your code should go here:

from math import log

def solveExp(a, b):
    return round(log(b, a))

print(solveExp(4, 1024))
print(solveExp(2, 1024))
print(solveExp(9, 3486784401))
print(solveExp(9, 81))

# The program is complete.