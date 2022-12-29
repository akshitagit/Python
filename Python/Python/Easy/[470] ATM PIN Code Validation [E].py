"""
##ATM PIN Code Validation

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. Your task is to create a function that takes a string and returns True if the PIN is valid and False if it's not.


[Examples]

___
is_valid_PIN("1234") ➞ True

is_valid_PIN("12345") ➞ False

is_valid_PIN("a234") ➞ False

is_valid_PIN("") ➞ False
_____



[Notes]

___
*) Some test cases contain special characters.
*) Empty strings must return False.
___



[regex] [validation] 



-------------------------------------------------------------------
[Resources]
_________
isdigit() Method
https://www.tutorialspoint.com/python/string_isdigit.htm
Checks whether the string consists of digits only.
_________
_________
Learn Regular Expressions
https://regexone.com/references/python
RegexOne provides a set of interactive lessons and exercises to help you learn regular expressions.
_________
_________
How to Use Python's len() Method
https://www.pythoncentral.io/how-to-use-pythons-len-method/
Learn how to find the length of a string easily with Python's len() method.
_________
_________
len() Method
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) of an object.
_________
_________
Difference between string isdecimal(), isdigit() and isnumeric() methods
https://www.includehelp.com/python/difference-between-string-isdecimal-isdigit-isnumeric-and-methods.aspx
The methods isdigit(), isnumeric() and isdecimal() are in-built methods of String in python programming language, which are worked with strings as Unicode objects. Thes …
_________
_________
isnumeric
https://www.geeksforgeeks.org/python-string-isnumeric-application/
Checks an entire string to determine whether an entire string contains only numeric characters.
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
.span() returns a tuple containing the start-, and end positions of the match. .string returns the string passed into the function .group() returns the part of the st …
_________
_________
re.fullmatch Python Example
https://www.programcreek.com/python/example/96665/re.fullmatch
The following are code examples for showing how to use re.fullmatch(). They are extracted from open source Python projects. You can vote up the examples you like or vot …
_________
_________
Regular Expressions
https://www.tutorialspoint.com/python/python_reg_expressions.htm
Is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pat...
_________
""" 
# Your code should go here:

