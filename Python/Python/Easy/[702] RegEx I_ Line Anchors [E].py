"""
####  RegEx I: Line Anchors  ####

Regular Expressions (RegEx) are a powerful tool used to match or search for a pattern in a string. To use them in Python you need to import the re module. You can do this by adding the following line at the top of your file:
___
import re
_____

Write a regular expression that will match the files with the extension .py or .pyw. You must use the RegEx line anchor $, which matches the end of a string.


[Examples]

___
pattern = "yourregularexpressionhere"

bool(re.search(pattern, "/users/file.py")) ➞ True
bool(re.search(pattern, "/users/file.pyw")) ➞ True
bool(re.search(pattern, "/users/python/file.txt")) ➞ False
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and line anchors in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[formatting] [regex] [validation] 



-------------------------------------------------------------------
[Resources]
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
Regular Expression Library
http://regexlib.com/Search.aspx?k=file+path&AspxAutoDetectCookieSupport=1
Lots of examples.
_________
_________
Regular Expression Anchors
https://www.rexegg.com/regex-anchors.html
Regex anchors. Presents regular expression anchors and discusses their behavior in various programming languages.
_________
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________

"""
#Your code should go here:

