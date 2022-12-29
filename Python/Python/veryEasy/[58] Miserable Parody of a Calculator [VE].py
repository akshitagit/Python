"""
##Miserable Parody of a Calculator

Create a function that will handle simple math expressions. The input is an expression in the form of a string.


[Examples]

___
calculator("23+4") ➞ 27

calculator("45-15") ➞ 30

calculator("13+2-5*2") ➞ 5

calculator("49/7*2-3") ➞ 11
_____



[Notes]

___
*) There will be no brackets in the input line.
*) No need to calculate mathematical functions (sin, cos, ln...).
*) There are no gaps in the expression.
___



[algebra] [math] [strings] 



-------------------------------------------------------------------
[Resources]
_________
eval() Method
https://www.programiz.com/python-programming/methods/built-in/eval
Parses the expression passed to this method and runs python expression (code) within the program.
_________
_________
Evaluate Expressions Dynamically
https://realpython.com/python-eval-function/
In this step-by-step tutorial, you'll learn how Python's eval() works and how to use it effectively in your programs. Additionally, you'll learn how to minimize the sec …
_________
_________
What does Python's eval() do?
https://stackoverflow.com/questions/9383740/what-does-pythons-eval-do
Interprets a string as code. The reason why so many people have warned you about using this is because a user can use this as an option to run code on the computer. If …
_________
""" 
# Your code should go here:

def exCalc(exp1):
    return (int(eval(exp1)))

print(exCalc("23+4"))
print(exCalc("45-15"))
print(exCalc("13+2-5*2"))
print(exCalc("49/7*2-3"))

# This program is complete.