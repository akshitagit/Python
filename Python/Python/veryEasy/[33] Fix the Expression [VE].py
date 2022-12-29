"""
##Fix the Expression

Fix the code in the Code tab so the function returns true if and only if x is equal to 7. Try to debug code and pass all the tests.


[Examples]

___
is_seven(4) ➞ False

is_seven(9) ➞ False

is_seven(7) ➞ True
_____



[Notes]

The bug can be hard to find, so look closely!


[bugs] [language_fundamentals] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Booleans
https://www.w3schools.com/python/python_booleans.asp
In programming you often need to know if an expression is True or False. You can evaluate any expression in Python, and get one of two answers, True or False. When yo …
_________
_________
R if...else Statement
https://www.datamentor.io/r-programming/if-else-statement/
Decision making is an important part of programming. This can be achieved in R programming using the conditional if...else statement.
_________
_________
Comparison Operators
https://data-flair.training/blogs/python-comparison-operators/
Learn Python less than, Python greater than, equal to, not equal to less than, greater than or equal to Operators syntax.
_________
_________
Conditions
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics. These conditions can be used in several ways, most commonly in "if statements" and loops. An "if stateme …
_________
_________
if Statement in a Single Line Syntax
https://thispointer.com/python-if-else-in-one-line-a-ternary-operator/
if-else statement in a single line.
_________
""" 
# Your code should go here:

def isSeven(num1):
    if num1 == 7:
        return True
    else:
        return False

print(isSeven(4))
print(isSeven(9))
print(isSeven(7))
print(isSeven(0))

# The program is complete.