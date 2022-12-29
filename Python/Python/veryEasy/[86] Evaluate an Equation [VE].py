"""
##Evaluate an Equation

Create a function that evaluates an equation.


[Examples]

___
eq("1+2") ➞ 3

eq("6/(9-7)") ➞ 3

eq("3+2-4") ➞ 1
_____



[Notes]

___
*) Don't print, return a value.
*) Return the value, not the equation.
*) The method used to solve this challenge should not be used in practice.
However, it's important to be aware of how this functionality works and why it should not be used. Check the Resources for more information.
___



[math] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
eval() Method
https://www.geeksforgeeks.org/eval-in-python/
This article discusses a built-in function in Python, eval. It is an interesting hack/utility in Python which lets a Python program run Python code within itself. The …
_________
_________
eval() Function
https://www.w3schools.com/python/ref_func_eval.asp
Evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
_________
_________
str() Method
https://www.w3resource.com/python/built-in-function/str.php
Used to convert the specified value into a string.
_________
""" 
# Your code should go here:

eqEval = lambda equation1 : eval(equation1)

print(eqEval("1+2"))
print(eqEval("6/(9-7)"))
print(eqEval("3+2-4"))

# The program is complete.