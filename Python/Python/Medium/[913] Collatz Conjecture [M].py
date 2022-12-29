"""
####  Collatz Conjecture  ####

A Collatz sequence is generated like this. Start with a positive number. If it's even, halve it. If it's odd, multiply it by three and add one. Repeat the process with the resulting number. The Collatz Conjecture is that every sequence eventually reaches 1 (continuing past 1 just results in an endless repeat of the sequence 4, 2, 1).
The length of the sequence from starting number to 1 varies widely.
Create a function that takes a number as an argument and returns a tuple of two elements — the number of steps in the Collatz sequence of the number, and the highest number reached.


[Examples]

___
collatz(2) ➞ (2, 2)
# seq = [2, 1]

collatz(3) ➞ (8, 16)
# seq = [3, 10, 5, 16, 8, 4, 2, 1]

collatz(7) ➞ (17, 52)
# seq = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

collatz(8) ➞ (4, 8)
# seq = [8, 4, 2, 1]
_____



[Notes]

(Improbable) Bonus: Find a positive starting number that doesn't reach 1, and score a place in Math history plus a cash prize.


[control_flow] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Collatz Conjecture
https://en.wikipedia.org/wiki/Collatz_conjecture
A conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows …
_________
_________
Python "while" Loops (Indefinite Iteration)
https://realpython.com/python-while-loop/
In this tutorial, you'll learn about indefinite iteration using the Python while loop. You’ll be able to construct basic and complex while loops, interrupt loop executi …
_________

"""
#Your code should go here:

