"""
####  Slidey Numbers  ####

A number is considered slidey if for every digit in the number, the next digit from that has an absolute difference of one. Check the examples below.


[Examples]

___
is_slidey(123454321) ➞ True

is_slidey(54345) ➞ True

is_slidey(987654321) ➞ True

is_slidey(1123) ➞ False

is_slidey(1357) ➞ False
_____



[Notes]

___
*) A number cannot slide properly if there is a "flat surface" (example #4), or has gaps (example #5).
*) All single digit numbers can be considered slidey numbers!
___



[numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
all() & any() Functions
https://www.tutorialspoint.com/any-and-all-in-python
The any() function returns True if any item in an iterable are true, otherwise it returns False. However, if the iterable object is empty, the any () function will retu …
_________
_________
abs() Method
https://www.geeksforgeeks.org/abs-in-python/
Used to return the absolute value of a number.
_________
_________
Python zip()
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and return it.
_________

"""
#Your code should go here:

