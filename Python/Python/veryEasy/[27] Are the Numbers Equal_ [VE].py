"""
##Are the Numbers Equal?

Create a function that returns True when num1 is equal to num2; otherwise return False.


[Examples]

___
is_same_num(4, 8) ➞ False

is_same_num(2, 2) ➞  True

is_same_num(2, "2") ➞ False
_____



[Notes]

Don't forget to return the result.


[conditions] [language_fundamentals] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Conditions and If Statements
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics: Equals: a == b Not Equals: a != b Less than: a < b Less than or equal to: a <= b Greater than: a > b Gre …
_________
_________
if, if...else, if...elif...else and Nested if Statement
https://www.programiz.com/python-programming/if-elif-else
In this article, you will learn to create decisions in a Python program using different forms of if..else statement.
_________
_________
If Statements
http://anh.cs.luc.edu/handsonPythonTutorial/ifstatements.html
The general Python syntax for a simple if statement is. if condition : indentedStatementBlock. If the condition is true, then do the indented statements.
_________
""" 
# Your code should go here:

def numsSame(num1, num2):
    if num1 == num2:
        return True
    else:
        return False

print(numsSame(2,2)) # True
print(numsSame(3,4)) # False
print(numsSame(2, "2")) # False
print(numsSame(3, "3")) # False
print(numsSame(0, 0)) # True

# The program is complete.