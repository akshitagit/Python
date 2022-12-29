"""
####  Double Factorial  ####

Create a function that takes a number num and returns its double factorial. Mathematically, the formulas for double factorial are as follows.
If num is even:
___
num !! = num (num - 2)(num - 4)(num - 6) ... (4)(2)
_____

If num is odd:
___
num !! = num (num - 2)(num - 4)(num - 6) ... (3)(1)
_____

If num = 0 or num = -1, then num !! = 1 by convention.


[Examples]

___
double_factorial(0) ➞ 1

double_factorial(2) ➞ 2

double_factorial(9) ➞ 945
# 9*7*5*3*1 = 945

double_factorial(14) ➞ 645120
_____



[Notes]

___
*) Assume all input values are greater than or equal to -1.
*) Try to solve it with recursion.
*) Double factorial is not the same as factorial * 2.
___



[numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
double factorial
https://whatis.techtarget.com/definition/double-factorial
Is a quantity defined for all integer s greater than or equal to -1. For an even integer n , the double factorial is the product of all even integers less than or equal …
_________
_________
How do you a double factorial in python?
https://stackoverflow.com/questions/4740172/how-do-you-a-double-factorial-in-python#:~:text=Double%20factorial%20For%20an%20even,than%20or%20equal%20to%20p.
Isn't that just the same as the factorial with a different ending condition and a different parameter to the recursion call? def doublefactorial(n): if n <= 0: …
_________

"""
#Your code should go here:

