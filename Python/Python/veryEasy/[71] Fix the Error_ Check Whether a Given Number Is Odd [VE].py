"""
##Fix the Error: Check Whether a Given Number Is Odd

Éowyn has written the function is_odd() to check if a given number is odd or not.
Unfortunately, the function does not return the correct result for all the inputs. Help her fix the error.
___
def is_odd(num):
  return num % 1 == 1 or 2
_____



[Examples]

___
is_odd(-5) ➞ True

is_odd(25) ➞ True

is_odd(0) ➞ False
_____



[Notes]

All the inputs will only be integers.


[bugs] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Check if a Number is Odd or Even
https://www.programiz.com/python-programming/examples/odd-even
A number is even if it is perfectly divisible by 2. When the number is divided by 2, we use the remainder operator % to compute the remainder. If the remainder is not z …
_________
_________
How to check if a number is odd or even in Python?
https://stackoverflow.com/questions/21837208/check-if-a-number-is-odd-or-even-in-python
I'm trying to make a program which checks if a word is a palindrome and I've gotten so far and it works with words that have an even amount of numbers. I know how to ma …
_________
_________
Detecting Odd and Even
https://runestone.academy/runestone/books/published/StudentCSP/CSPTurtleDecisions/oddEven.html
If a number is evenly divisible by 2 with no remainder, then it is even. You can calculate the remainder with the modulo operator % like this num % 2 == 0. If a number …
_________
_________
abs() Function
https://www.geeksforgeeks.org/abs-in-python/
Is used to return the absolute value of a number. The abs() takes only one argument, a number whose absolute value is to be returned. The argument can be an integer, a …
_________
""" 
# Your code should go here:

# def isOdd(num):
#     return True if num % 2 == 1 else False

isOdd = lambda num : True if num % 2 == 1 else False

print(isOdd(-5))
print(isOdd(25))
print(isOdd(0))
print(isOdd(1000))
print(isOdd(2))

# The program is complete.