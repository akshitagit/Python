"""
####  N Differences  ####

Write a function that transforms an array into an array of its differences repeatedly until there exists only one element left. A difference is A[n+1] - A[n].
To illustrate:
___
[5, 1, 9, 3, 4, 0]

[-4, 8, -6, 1, -4]
# 1 - 5 = -4; 9 - 1 = 8; 3 - 9 = -6; etc.

[12, -14, 7, -5]

[-26, 21, -12]

[47, -33]

-80 
_____



[Examples]

___
n_differences([5, 1, 9, 3, 4, 0]) ➞ -80

n_differences([1, 1, 1, 1]) ➞ 0

n_differences([5, 8, 8]) ➞ -3
_____



[Notes]

Each array will have at least two elements.


[arrays] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Python Subtracting Elements in a Lists from Previous Element
https://stackoverflow.com/questions/39088546/python-subtracting-elements-in-a-lists-from-previous-element
I have a loop that produces multiple lists such as these: [1,6,2,8,3,4] [8,1,2,3,7,2] [9,2,5,6,1,4] For each list, I want to subtract the first two elements, and then u …
_________
_________
While Loop
https://www.programiz.com/python-programming/while-loop
Loops are used in programming to repeat a specific block of code. In this article, you will learn to create a while loop in Python.
_________
_________
zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
In this step-by-step tutorial, you'll learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables i …
_________

"""
#Your code should go here:

