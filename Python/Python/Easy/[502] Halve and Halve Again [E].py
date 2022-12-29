"""
##Halve and Halve Again

Given two integers a and b, return how many times a can be halved while still being greater than b.


[Examples]

___
halve_count(1324, 98) ➞ 3
# (1324 -> 662 -> 331 -> 165.5)

halve_count(624, 8) ➞ 6
# (624 -> 312 -> 156 -> 78 -> 39 -> 19.5 -> 9.75)

halve_count(1000, 3) ➞ 8
# (1000 -> 500 -> 250 -> 125 -> 62.5 -> 31.25 -> 15.625 -> 7.8125 -> 3.90625)
_____



[Notes]

Integer a will always be able to be halved at least once in every test case.


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How do you find nth term rule for 1/2,1/4,1/8,1/16,...?
https://socratic.org/questions/how-do-you-find-nth-term-rule-for-1-2-1-4-1-8-1-16
n^(th) term is 1/2^n. The series 1/2,1/4,1/8,1/16,.... can be written as 1/2^1,1/2^2,1/2^3,1/2^4,.... Hence n^(th) term can be written as 1/2^n. Other way could be to t …
_________
_________
N-th Term of Geometric Progression Series
https://www.geeksforgeeks.org/find-nth-term-geometric-progression-series/
Given first term (a), common ratio (r) and a integer N of the Geometric Progression series, the task is to find Nth term of the series.
_________
_________
The Sum of the Geometric Series 1 + 1/2 + 1/4
https://www.math.toronto.edu/mathnet/questionCorner/geomsum.html
This sequence of numbers (1, 3/2, 7/4, 15/8, . . . ) is converging to a limit. It is this limit which we call the "value" of the infinite sum.
_________
_________
Nth Term Of A Gp
https://www.cuemath.com/algebra/nth-term-of-a-gp/
Consider a GP with first term equal to a and common ratio equal to r. The second term will be a r , the third term will be a r 2 , the fourth term will be a r 3 , th …
_________
_________
Log Functions
https://www.geeksforgeeks.org/log-functions-python/
Python offers many inbuild logarithmic functions under the module “math” which allows us to compute logs using a single line. There are 4 variants of logarithmic functions.
_________
_________
How to calculate the number of times a number can be halved before reaching 1?
https://stackoverflow.com/questions/16201165/calculate-how-many-times-a-number-can-be-halved-before-reaching-1
The questions is to write a function that tells how many times n can be halves before reaching 1. I have been working on making this code work, but its not working. I t …
_________
""" 
# Your code should go here:

