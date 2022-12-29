"""
####  Divisible by Left Digit?  ####

Create a function that takes a number n and checks if each digit is divisible by the digit on its left. Return a boolean array depending on the condition checks.


[Examples]

___
divisible_by_left(73312) ➞ [False, False, True, False, True]
# no element left to 7 = False
# 3/7 = False
# 3/3 = True
# 1/3 = False
# 2/1 = True

divisible_by_left(1) ➞ [False]

divisible_by_left(635) ➞ [False, False, False]
_____



[Notes]

The array should always start with False as there is no digit to the left of the first digit.


[logic] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
List Comprehension
https://www.programiz.com/python-programming/list-comprehension
Suppose, we want to separate the letters of the word human and add the letters as items of a list. The first thing that comes in mind would be using for loop.
_________
_________
For Loops
https://www.w3schools.com/python/python_for_loops.asp
Used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other programming languages …
_________
_________
Conditions and If Statements
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics. These conditions can be used in several ways, most commonly in "if statements" and loops. An "if stateme …
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Operators are used to perform operations on variables and values. In the example below, we use the + operator to add together two values.
_________
_________
zip() Method
https://www.w3schools.com/python/ref_func_zip.asp
Returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator a …
_________

"""
#Your code should go here:

