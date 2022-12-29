"""
##Nth Even Number

Create a function that takes a number n and returns the nth even number beginning with 0 as the first.


[Examples]

___
nth_even(1) ➞ 0
# 0 is first even number

nth_even(2) ➞ 2
# 2 is second even number

nth_even(100) ➞ 198
_____



[Notes]

N/A


[language_fundamentals] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
List of Even Numbers
https://www.chilimath.com/lessons/introductory-algebra/list-of-even-numbers/
To review the concept of an even number, please check out my lesson on Even Numbers. You may click the image below with your mouse 🐭 to take you to the lesson.
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Operators are used to perform operations on variables and values.
_________
_________
Python Program to Print Even Numbers in a List
https://www.geeksforgeeks.org/python-program-to-print-even-numbers-in-a-list/
Given a list of numbers, write a Python program to print all even numbers in given list.
_________
""" 
# Your code should go here:

def nthEven(nth):
    a = range(0,(2*nth), 2)
    return a[-1]

print(nthEven(4))
print(nthEven(1))
print(nthEven(2))
print(nthEven(100))

# The program is complete.