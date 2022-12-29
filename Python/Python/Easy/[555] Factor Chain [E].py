"""
##Factor Chain

A factor chain is a list where each previous element is a factor of the next consecutive element. The following is a factor chain:
___
[3, 6, 12, 36]

# 3 is a factor of 6
# 6 is a factor of 12
# 12 is a factor of 36
_____

Create a function that determines whether or not a list is a factor chain.


[Examples]

___
factor_chain([1, 2, 4, 8, 16, 32]) ➞ True

factor_chain([1, 1, 1, 1, 1, 1]) ➞ True

factor_chain([2, 4, 6, 7, 12]) ➞ False

factor_chain([10, 1]) ➞ False
_____



[Notes]

N/A


[arrays] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
% modulus
https://python-reference.readthedocs.io/en/latest/docs/operators/modulus.html
Returns the decimal part (remainder) of the quotient.
_________
_________
any() all()
https://www.tutorialspoint.com/any-and-all-in-python
The any() function returns True if any item in an iterable are true, otherwise it returns False. However, if the iterable object is empty, the any () function will retu …
_________
_________
zip() Function
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and return it.
_________
_________
List Comprehensions in Python
https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
List comprehensions provide a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if claus …
_________
_________
Find All Divisors of a Natural Number
https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/
A naive solution would be to iterate all the numbers from 1 to n, checking if that number divides n and printing it. Below is program for the same. If we look carefully …
_________
""" 
# Your code should go here:

