"""
##Flip the Boolean

Due to a programming concept known as truthiness, certain values can be evaluated to (i.e. take the place of) booleans.
For example, 1 (or any number other than 0) is often equivalent to True, and 0 is often equivalent to False.
Create a function that returns the opposite of the given boolean, as a number.


[Examples]

___
flip_bool(True) ➞ 0

flip_bool(False) ➞ 1

flip_bool(1) ➞ 0

flip_bool(0) ➞ 1
_____



[Notes]

N/A


[conditions] [language_fundamentals] [logic] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Boolean Data Type
https://problemsolvingwithpython.com/04-Data-Types-and-Variables/04.02-Boolean-Data-Type/
The boolean data type is either True or False. In Python, boolean variables are defined by the True and False keywords.
_________
_________
Boolean Operations — and, or, not
https://docs.python.org/2/library/stdtypes.html
Official Python documentation explaining the Boolean data type.
_________
_________
Python Operators
https://www.geeksforgeeks.org/python-operators/
Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division.
_________
""" 
# Your code should go here:

def flipBool(boolVal):
    if boolVal == True:
        return int(0)
    elif boolVal == False:
        return int(1)
    else:
        return 0


print(flipBool(True))
print(flipBool(False))
print(flipBool(1))
print(flipBool(0))
print(flipBool(21))

# The program is complete.