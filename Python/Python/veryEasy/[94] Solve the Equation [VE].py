"""
##Solve the Equation

Create a function that takes an equation (e.g. "1+1"), and returns the answer.


[Examples]

___
equation("1+1") ➞ 2

equation("7*4-2") ➞ 26

equation("1+1+1+1+1") ➞ 5
_____



[Notes]

Supported operators are +, -, and *.


[language_fundamentals] [math] 



-------------------------------------------------------------------
[Resources]
_________
eval() Method
https://www.geeksforgeeks.org/eval-in-python/
Parses the expression passed to it and runs python expression(code) within the program.
_________
_________
Python eval() built-in-function
https://towardsdatascience.com/python-eval-built-in-function-601f87db191
Now you all know the input() takes the user input, but when the user enters an integer as an input the input function returns a string, but in the case of eval it will …
_________
""" 
# Your code should go here:

equational = lambda eqInput : eval(eqInput)

print(equational("1+1"))
print(equational("7*4-2"))
print(equational("2**3"))
print(equational("1+1+1+1+1"))

# The program is complete.