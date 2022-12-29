"""
####  Balanced List  ####

Given a list of even length, copy the half with the higher sum of numbers to the other half of the list. If the sum of the first half equals the sum of the second half, return the original list.


[Examples]

___
balanced([1, 2, 4, 6, 3, 1]) ➞ [6, 3, 1, 6, 3, 1]
# 1 + 2 + 4 < 6 + 3 + 1  sol = [6, 3, 1, 6, 3, 1]

balanced([88, 3, 27, 5, 9, 0, 13, 10]) ➞ [88, 3, 27, 5, 88, 3, 27, 5]
# 88 + 3 + 27 + 5 > 9 + 0 + 13 + 10  sol = [88, 3, 27, 5, 88, 3, 27, 5]

balanced([7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]) ➞ [7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]
# 7 + 5 + 2 + 6 + 1 + 0 = 1 + 5 + 2 + 7 + 0 + 6  sol =  [7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]
_____



[Notes]

The length of the list is even.


[arrays] [conditions] [math] 



-------------------------------------------------------------------
[Resources]
_________
if, if...else, if...elif...else and Nested if Statement
https://www.programiz.com/python-programming/if-elif-else
In this article, you will learn to create decisions in a Python program using different forms of if..else statement.
_________
_________
List Slicing
https://www.learnbyexample.org/python-list-slicing/
Learn to slice a list with positive & negative indices in Python, modify insert and delete multiple list items, reverse a list, copy a list and more.
_________
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________

"""
#Your code should go here:

