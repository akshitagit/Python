"""
####  Abbreviations Unique?  ####

You are given two inputs:

Write a function that returns True if each abbreviation uniquely identifies a word, and False otherwise.


[Examples]

___
unique_abbrev(["ho", "h", "ha"], ["house", "hope", "happy"]) ➞ False
// "ho" and "h" are ambiguous and can identify either "house" or "hope"

unique_abbrev(["s", "t", "v"], ["stamina", "television", "vindaloo"]) ➞ True

unique_abbrev(["bi", "ba", "bat"], ["big", "bard", "battery"]) ➞ False

unique_abbrev(["mo", "ma", "me"], ["moment", "many", "mean"]) ➞ True
_____



[Notes]

Abbreviations will be a substring from [0, n] from the original string.


[higher_order_functions] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Understanding Nested List Comprehension Syntax in Python
https://spapas.github.io/2016/04/27/python-nested-list-comprehensions/
List comprehensions are one of the really nice and powerful features of Python. It is actually a smart way to introduce new users to functional programming concepts (af …
_________
_________
startswith() Method
https://www.tutorialspoint.com/python3/string_startswith.htm
Checks whether the string starts with str, optionally restricting the matching with the given indices start and end.
_________

"""
#Your code should go here:

