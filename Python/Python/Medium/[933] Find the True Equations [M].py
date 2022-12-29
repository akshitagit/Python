"""
####  Find the True Equations  ####

In this challenge you will be given a list containing equations, with each equation written as a string. Here's an example:
___
["1+1=2", "2+2=3", "5*5=10", "3/3=1"]
_____

If you do the math, you'll see that the equations "1+1=2" and "3/3=1" are actually true while "2+2=3" and "5*5=10" are false nonsense.
Write a function which, given a list of equations as above, returns only the true equations. For instance, for the example above the output should be:
___
["1+1=2", "3/3=1"]
_____



[Examples]

___
true_equations(["2*2=4"]) ➞ ["2*2=4"]

true_equations(["1+1=3", "3-1=1"]) ➞ []

true_equations(["1+1=2", "2+2=3", "5*5=10", "3/3=1"]) ➞ ["1+1=2", "3/3=1"]
_____



[Notes]

___
*) If all equations are false, return the empty list [], as in the second example.
*) The equations will only involve the elementary operations: +, -, *, /
___



[algebra] [language_fundamentals] [math] [strings] 



-------------------------------------------------------------------
[Resources]
_________
split() Method
https://www.w3schools.com/python/ref_string_split.asp
Splits a string into a list.
_________
_________
replace() Method
https://www.w3schools.com/python/ref_string_replace.asp
Replaces a specified phrase with another specified phrase.
_________
_________
eval() Method
https://www.w3schools.com/python/ref_func_eval.asp
Evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
_________

"""
#Your code should go here:

