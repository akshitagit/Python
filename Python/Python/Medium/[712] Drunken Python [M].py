"""
####  Drunken Python  ####

Python got drunk and the built-in functions str() and int() are acting odd:
___
str(4) ➞ 4

str("4") ➞ 4

int("4") ➞ "4"

int(4) ➞ "4"
_____

You need to create two functions to substitute str() and int(). A function called int_to_str() that converts integers into strings and a function called str_to_int() that converts strings into integers.


[Examples:]

___
int_to_str(4) ➞ "4"

str_to_int("4") ➞ 4

int_to_str(29348) ➞ "29348"
_____



[Notes]

___
*) This is meant to illustrate the dangers of using already-existing function names.
*) Extra points if you can de-drunk Python.
___



[language_fundamentals] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python Anti-Patterns
https://docs.quantifiedcode.com/python-anti-patterns/correctness/assigning_to_builtin.html
In the code below, the list built-in is overwritten. This makes it impossible, to use list to define a variable as a list. As this is a very concise example, it is easy …
_________
_________
How to Convert a Python String to int
https://realpython.com/convert-python-string-to-int/
Integers are whole numbers. In other words, they have no fractional component. Two data types you can use to store an integer in Python are int and str. These types off …
_________
_________
Python str() and int() tutorial| Career Karma
https://careerkarma.com/blog/python-string-to-int/#:~:text=The%20int()%20method%20is,an%20integer%20to%20a%20string.
The Python int method is used to convert a string to an integer. Learn how to use the int and str method on Career Karma.
_________
_________
Convert String to Integer in Python
https://www.geeksforgeeks.org/convert-string-to-integer-in-python/
In Python an strings can be converted into a integer using the built-in int() function. The int() function takes in any python data type and converts it into a integer.
_________
_________
format() Function
https://www.educba.com/python-format-function/
Guide to Python format() Function. Here we discuss the Introduction to Python format() Function along with different examples.
_________

"""
#Your code should go here:

