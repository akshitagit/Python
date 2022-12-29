"""
####  Valid Hex Code  ####

Create a function that determines whether a string is a valid hex code.
A hex code must begin with a pound key # and is exactly 6 characters in length. Each character must be a digit from 0-9 or an alphabetic character from A-F. All alphabetic characters may be uppercase or lowercase.


[Examples]

___
is_valid_hex_code("#CD5C5C") ➞ True

is_valid_hex_code("#EAECEE") ➞ True

is_valid_hex_code("#eaecee") ➞ True

is_valid_hex_code("#CD5C58C") ➞ False
# Length exceeds 6

is_valid_hex_code("#CD5C5Z") ➞ False
# Not all alphabetic characters in A-F

is_valid_hex_code("#CD5C&C") ➞ False
# Contains unacceptable character

is_valid_hex_code("CD5C5C") ➞ False
# Missing #
_____



[Notes]

N/A


[regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________
_________
RegExr: Learn, Build, & Test RegEx
https://regexr.com/
An online tool to learn, build, & test Regular Expressions (RegEx / RegExp).
_________
_________
Logical Operators
https://www.w3schools.com/python/python_operators.asp
Operators are used to perform operations on variables and values. In the example, we use the + operator to add together two values...
_________

"""
#Your code should go here:

