"""
##The Farm Problem

In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:
___
*) chickens = 2 legs
*) cows = 4 legs
*) pigs = 4 legs
___

The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.


[Examples]

___
animals(2, 3, 5) ➞ 36

animals(1, 2, 3) ➞ 22

animals(5, 2, 8) ➞ 50
_____



[Notes]

___
*) Don't forget to return the result.
*) The order of animals passed is animals(chickens, cows, pigs).
*) Remember that the farmer wants to know the total number of legs and not the total number of animals.
___



[algorithms] [language_fundamentals] [math] 



-------------------------------------------------------------------
[Resources]
_________
Python Operators
https://www.datacamp.com/community/tutorials/python-operators-tutorial
This tutorial covers the different types of operators in Python, operator overloading, precedence and associativity.
_________
_________
Python Lists
https://www.geeksforgeeks.org/python-list/
Lists are just like the arrays, declared in other languages. Lists need not be homogeneous always which makes it a most powerful tool in Python. A single list may conta …
_________
_________
Python Basic Operators
https://www.tutorialspoint.com/python/python_basic_operators.htm
Operators are the constructs which can manipulate the value of operands. Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.
_________
_________
How to Use Python Lambda Functions
https://realpython.com/python-lambda/
Learn about Python lambda functions. You'll see how they compare with regular functions and how you can use them in accordance with best practices.
_________
""" 
# Your code should go here:

def totalLegCount(chickens, cows, pigs):
    return ((chickens * 2) + (cows * 4) + (pigs * 4))

print(totalLegCount(2, 3, 5))
print(totalLegCount(1, 2, 3))
print((totalLegCount(5, 2, 8)))

# The program is complete.