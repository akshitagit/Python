"""
##Buggy Code (Part 2)

Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to get an idea of what the function should do.


[Examples]

___
max_num(3, 7) ➞ 7

max_num(-1, 0) ➞ 0

max_num(1000, 400) ➞ 1000
_____



[Notes]

___
*) READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!
*) Don't overthink this challenge; it's not supposed to be hard.
___



[bugs] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Python Conditions and If statements
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics. These conditions can be used in several ways, most commonly in "if statements" and loops. An "if stateme …
_________
_________
Conditional Statements
https://realpython.com/python-conditional-statements/
In this step-by-step tutorial you'll learn how to work with conditional ("if") statements in Python. Master if-statements step-by-step and see how to write complex deci …
_________
_________
Functions that Return Values
https://runestone.academy/runestone/books/published/thinkcspy/Functions/Functionsthatreturnvalues.html
Most functions require arguments, values that control how the function does its job. For example, if you want to find the absolute value of a number, you have to indica …
_________
_________
max() Function
https://www.programiz.com/python-programming/methods/built-in/max
Returns the largest item in an iterable. It can also be used to find the largest item between two or more parameters.
_________
""" 
# Your code should go here:

def maxNum(num1, num2):
    list1 = [num1, num2]
    return max(list1)

print(maxNum(3, 7))
print(maxNum(-1, 0))
print(maxNum(600, 1000))
print(maxNum(2,2))
print(maxNum(10000,100))

# The program is complete.