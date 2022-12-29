"""
##Upper or Lower Case

Return the smallest number of steps it takes to convert a string entirely into uppercase or entirely into lower case, whichever takes the fewest number of steps. A step consists of changing one character from lower to upper case, or vice versa.


[Examples]

___
steps_to_convert("abC") ➞ 1
# "abC" converted to "abc" in 1 step

steps_to_convert("abCBA") ➞ 2
# "abCBA" converted to "ABCBA" in 2 steps

steps_to_convert("aba") ➞ 0

steps_to_convert("abaCCC") ➞ 3
_____



[Notes]

___
*) Return 0 if empty string.
*) Return 0 if the string is already entirely in one case.
*) Only alphabetic characters.
*) Input has no spaces.
___



[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
isupper(), islower(), lower(), upper() in Python and their applications
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
In Python, isupper() is a built-in method used for string handling. The isupper() methods returns “True” if all characters in the string are uppercase, Otherwise, It re …
_________
_________
Python Strings
https://thepythonguru.com/python-strings/
Are contiguous series of characters delimited by single or double quotes. Python doesn’t have any separate data type for characters so they are represented as a single …
_________
_________
Count the uppercase letters in a string with Python
https://stackoverflow.com/questions/18129830/count-the-uppercase-letters-in-a-string-with-python
I am trying to figure out how I can count the uppercase letters in a string. I have only been able to count lowercase letters.
_________
_________
min() Function
https://www.programiz.com/python-programming/methods/built-in/min
Returns the smallest item in an iterable. It can also be used to find the smallest item between two or more parameters.
_________
_________
Common String Operations
https://docs.python.org/3/library/string.html
The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.
_________
""" 
# Your code should go here:

