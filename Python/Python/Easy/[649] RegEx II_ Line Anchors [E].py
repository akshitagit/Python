"""
####  RegEx II: Line Anchors  ####

Regular Expressions (RegEx) are a powerful tool used to match or search for a pattern in a string. To use them in Python you need to import the re module. You can do this by adding the following line at the top of your file:
___
import re
_____

Write a regular expression that will match any file located within the "users/edabit" directory. You must use at least one RegEx line anchor.


[Examples]

___
pattern = "yourregularexpressionhere"

bool(re.search(pattern, "/users/edabit/python/regex.py")) ➞ True
bool(re.search(pattern, "/users/edabitt/python/file.txt")) ➞ False
bool(re.search(pattern, "/users/pyter/edabit/file.py")) ➞ False
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and line anchors in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[arrays] [formatting] [regex] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Regular Expression Anchors
https://www.rexegg.com/regex-anchors.html
Anchors belong to the family of regex tokens that don't match any characters, but that assert something about the string or the matching process. Anchors assert that th …
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
Python has a built-in package called re, which can be used to work with Regular Expressions.
_________
_________
Online Regex Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
_________
Regular Expressions
https://www.tutorialspoint.com/python/python_reg_expressions.htm
Is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions are …
_________
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________

"""
#Your code should go here:

