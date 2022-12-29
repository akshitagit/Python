"""
##Magic Date

You are to read each part of the date into its own integer type variable. The year should be a 4 digit number. You can assume the user enters a correct date (no error checking required).
Determine whether the entered date is a magic date. Here are the rules for a magic date:
___
*) mm * dd is a 1-digit number that matches the last digit of yyyy or
*) mm * dd is a 2-digit number that matches the last 2 digits of yyyy or
*) mm * dd is a 3-digit number that matches the last 3 digits of yyyy
___

The program should then display True if the date is magic, or False if it is not.


[Examples]

___
magic("1 1 2011") ➞ True

magic("4 1 2001") ➞ False

magic("5 2 2010") ➞ True

magic("9 2 2011") ➞ False
_____



[Notes]

N/A


[dates] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
endswith()
https://www.programiz.com/python-programming/methods/string/endswith
Returns True if a string ends with the specified suffix. If not, it returns False.
_________
_________
Regular Expression Operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations. Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). How …
_________
_________
Python RegExp - findall, search, and match
https://howchoo.com/g/zdvmogrlngz/python-regexes-findall-search-and-match
This guide will cover the basics of how to use three common regex functions in Python - findall, search, and match.
_________
_________
Multiple Assignment and Tuple Unpacking Improve Python Readability
https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
Whether I’m teaching new Pythonistas or long-time Python programmers, I frequently find that Python programmers underutilize multiple assignment. Multiple assignment ( …
_________
_________
How to Slice Lists/Arrays and Tuples in Python
https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
So you've got an list, tuple or array and you want to get specific sets of sub-elements from it, without any long, drawn out for loops? Python has an amazing feature ju …
_________
_________
Converting Strings to Datetime
https://stackabuse.com/converting-strings-to-datetime-in-python/
In this tutorial, we'll be converting Strings to datetime in Python, dealing with Timezones. We'll also use dateutil, Maya and Arrow to convert Strings to datetime.
_________
""" 
# Your code should go here:

