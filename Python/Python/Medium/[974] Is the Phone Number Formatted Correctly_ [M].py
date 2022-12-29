"""
####  Is the Phone Number Formatted Correctly?  ####

Create a function that accepts a string and returns True if it's in the format of a proper phone number and False if it's not. Assume any number between 0-9 (in the appropriate spots) will produce a valid phone number.
This is what a valid phone number looks like:
___
(123) 456-7890
_____



[Examples]

___
is_valid_phone_number("(123) 456-7890") ➞ True

is_valid_phone_number("1111)555 2345") ➞ False

is_valid_phone_number("098) 123 4567") ➞ False
_____



[Notes]

Don't forget the space after the closing parenthesis.


[formatting] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Python Regular Expressions
https://www.tutorialspoint.com/python/python_reg_expressions.htm
Python Regular Expressions - Learning Python in simple and easy steps : A beginner's tutorial containing complete knowledge of Python Syntax Object Oriented Language, M …
_________
_________
slicing
https://www.geeksforgeeks.org/string-slicing-in-python/
Is about obtaining a sub-string from the given string by slicing it respectively from start to end. Python slicing can be done in two ways. slice() Constructor Extendi …
_________
_________
format() Method
https://www.w3schools.com/python/gloss_python_string_format.asp
Takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
_________
_________
isalnum() Method
https://www.w3schools.com/python/ref_string_isalnum.asp
Returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
_________
_________
Regular Expression Operations
https://docs.python.org/3/library/re.html#match-objects
Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot be mixed: that …
_________

"""
#Your code should go here:

