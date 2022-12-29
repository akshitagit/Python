"""
##Filter Repeating Character Strings

Create a function that keeps only strings with repeating identical characters (in other words, it has a set size of 1).


[Examples]

___
identical_filter(["aaaaaa", "bc", "d", "eeee", "xyz"])
➞ ["aaaaaa", "d", "eeee"]

identical_filter(["88", "999", "22", "545", "133"])
➞ ["88", "999", "22"]

identical_filter(["xxxxo", "oxo", "xox", "ooxxoo", "oxo"])
➞ []
_____



[Notes]

___
*) A string with a single character is trivially counted as a string with repeating identical characters.
*) If there are no strings with repeating identical characters, return an empty array (see example #3).
___



[arrays] [language_fundamentals] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to check if string consists of one character in Python?
https://stackoverflow.com/questions/14320909/efficiently-checking-that-string-consists-of-one-character-in-python/14320949#14320949
What is an efficient way to check that a string s in Python consists of just one character, say 'A'? Something like all_equal(s, 'A') which would behave like this: all_ …
_________
_________
set() Constructor
https://www.programiz.com/python-programming/methods/built-in/set
Constructs a Python set from the given iterable and returns it.
_________
""" 
# Your code should go here:

