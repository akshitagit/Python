"""
####  Unusual Subtraction  ####

Create a function that subtracts 1 from n (unless it ends in 0) k number of times. If n ends in 0, remove the 0.
To illustrate:
___
n = 22
k = 3
_____

This means our number is 22 and we have to repeat the algorithm three times. 22 does not end in 0 so we continue subtracting 1.
___
22 - 1 = 21
k = 1
21 - 1 = 20
k = 2
_____

Now 20 ends in 0, so we can remove it. We get 2; k = 3. The algorithm ends there because we applied it three times.
___
N:  K:
22
21  1
20  2
2   3
_____



[Examples]

___
not_good_math(540, 5) ➞ 50

not_good_math(1000000000, 9) ➞ 1

not_good_math(42023110, 10) ➞ 4201
_____



[Notes]

Check resources!!


[algorithms] [logic] [math] 



-------------------------------------------------------------------
[Resources]
_________
Loops in Python
https://www.learnpython.org/en/Loops
There are two types of loops in Python, for and while. For loops can iterate over a sequence of numbers using the "range" and "xrange" functions. The difference between …
_________
_________
Ternary Operator in Python
https://www.geeksforgeeks.org/ternary-operator-in-python/
Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in versio …
_________
_________
Wrong Subtraction Question
https://codeforces.com/problemset/problem/977/A
Little girl Tanya is learning how to decrease a number by one, but she does it wrong with a number consisting of two or more digits. Tanya subtracts one from a number b …
_________

"""
#Your code should go here:

