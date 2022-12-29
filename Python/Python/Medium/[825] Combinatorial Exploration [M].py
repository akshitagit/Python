"""
####  Combinatorial Exploration  ####

Given a known number of unique items, how many ways could we arrange them in a row?
Create a function that takes an integer n and returns the number of digits of the number of possible permutations for n unique items. For instance, 5 unique items could be arranged in 120 unique ways. 120 has 3 digits, hence the integer 3 is returned.


[Examples]

___
no_perms_digits(0) ➞ 1

no_perms_digits(1) ➞ 1

no_perms_digits(5) ➞ 3

no_perms_digits(8) ➞ 5
_____



[Notes]

This challenge requires some understanding of combinatorics.


[higher_order_functions] [math] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
math.factorial()
https://www.geeksforgeeks.org/factorial-in-python/
Not many people know, but python offers a direct function that can compute the factorial of a number without writing the whole code for computing factorial.
_________
_________
Combinatorics
https://en.wikipedia.org/wiki/Combinatorics
An area of mathematics primarily concerned with counting, both as a means and an end in obtaining results, and certain properties of finite structures. It is closely re …
_________
_________
Combinatorial Explosion
https://en.wikipedia.org/wiki/Combinatorial_explosion
The bane of brute-force computing, this Wikipedia entry provides more information on a common phenomenon known as the combinatorial explosion.
_________
_________
Permutations Calculator nPr
https://www.calculatorsoup.com/calculators/discretemathematics/permutations.php
Find the number of ways of getting an ordered subset of r elements from a set of n elements as nPr (or nPk). Permutations calculator and permutations formula. Free onli …
_________
_________
How to find length of digits in an integer?
https://stackoverflow.com/questions/2189800/how-to-find-length-of-digits-in-an-integer
If you want the length of an integer as in the number of digits in the integer, you can always convert it to string like str(133) and find its length like len(str(123)).
_________

"""
#Your code should go here:

