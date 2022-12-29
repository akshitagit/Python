"""
##Travelling Salesman Problem

A salesman has a number of cities to visit. They want to calculate the total number of possible paths they could take, visiting each city once before returning home. Return the total number of possible paths a salesman can travel, given n cities.
If we have cities A, B and C, possible paths would be:
___
A -> B -> C
A -> C -> B
B -> A -> C
B -> C -> A
C -> B -> A
C -> A -> B
_____

... which gives us 6 as the possible number of paths.


[Examples]

___
paths(4) ➞ 24

paths(1) ➞ 1

paths(9) ➞ 362880
_____



[Notes]

___
*) Inspired by a video from Dr. Peter Uelkes.
*) This challenge is describing a factorial.
___



[algorithms] [logic] [math] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
math.factorial() function
https://www.geeksforgeeks.org/python-math-factorial-function/
In Python, math module contains a number of mathematical operations, which can be performed with ease using the module. math.factorial() function returns the factorial …
_________
_________
Combinations and Permutations
https://www.mathsisfun.com/combinatorics/combinations-permutations.html
First we should understand that the challenge requires us to find the permutation, given the number of paths. And this page explains what permutation is and its formula.
_________
_________
Itertools.permutations()
https://www.geeksforgeeks.org/python-itertools-permutations/
Falls under the Combinatoric Generators. The recursive generators that are used to simplify combinatorial constructs such as permutations, combinations, and Cartesian p …
_________
""" 
# Your code should go here:

