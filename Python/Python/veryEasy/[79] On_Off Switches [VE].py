"""
##On/Off Switches

Create a function that returns how many possible arrangements can come from a certain number of switches (on / off). In other words, for a given number of switches, how many different patterns of on and off can we have?


[Examples]

___
pos_com(1) ➞ 2

pos_com(3) ➞ 8

pos_com(10) ➞ 1024
_____



[Notes]

All numbers will be whole and positive.


[algebra] [logic] [math] 



-------------------------------------------------------------------
[Resources]
_________
Combinations and Permutations
https://www.mathsisfun.com/combinatorics/combinations-permutations.html
In English we use the word "combination" loosely, without thinking if the order of things is important. In other words: "My fruit salad is a combination of apples, grap …
_________
_________
Exponent **
https://www.programiz.com/python-programming/operators
Left operand raised to the power of right.
_________
_________
Python Operators
https://www.programiz.com/python-programming/operators
In this tutorial, you'll learn everything about different types of operators in Python, their syntax and how to use them with examples.
_________
_________
Permutation and Combination in Python
https://www.geeksforgeeks.org/permutation-and-combination-in-python/
Python provide direct methods to find permutations and combinations of a sequence. These methods are present in itertools package. First import itertools package to imp …
_________
""" 
# Your code should go here:

diffOnOffPatterns = lambda nSwitches : 2 ** nSwitches

print(diffOnOffPatterns(1))
print(diffOnOffPatterns(3))
print(diffOnOffPatterns(10))
print(diffOnOffPatterns(0))

# The program is complete.