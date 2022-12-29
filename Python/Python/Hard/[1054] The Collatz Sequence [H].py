"""
####  The Collatz Sequence  ####

The Collatz sequence is as follows:
___
*) Start with some given integer n.
*) If it is even, the next number will be n divided by 2.
*) If it is odd, multiply it by 3 and add 1 to make the next number.
*) The sequence stops when it reaches 1.
___

According to the Collatz conjecture, it will always reach 1. If that's true, you can construct a finite sequence following the aforementioned method for any given integer.
Write a function that takes in an integer n and returns the highest integer in the corresponding Collatz sequence.


[Examples]

___
max_collatz(10) ➞ 16
# Collatz sequence: 10, 5, 16, 8, 4, 2, 1

max_collatz(32) ➞ 32
# Collatz sequence: 32, 16, 8, 4, 2, 1

max_collatz(85) ➞ 256
# Collatz sequence: 85, 256, 128, 64, 32, 16, 8, 4, 2, 1
_____



[Notes]

N/A


[algorithms] [conditions] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
append() Method
https://www.programiz.com/python-programming/methods/list/append
Adds an item to the end of the list. In this tutorial, we will learn about the Python append() method in detail with the help of examples.
_________
_________
max() Function
https://www.programiz.com/python-programming/methods/built-in/max
Returns the largest item in an iterable. It can also be used to find the largest item between two or more parameters.
_________
_________
Collatz Conjecture
https://en.wikipedia.org/wiki/Collatz_conjecture
A conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows …
_________

"""
#Your code should go here:

