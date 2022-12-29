"""
####  RegEx XVI: Negation  ####

The caret ^, when found at the start of a character set, is the equivalent to "not" in RegEx. The regular expression [^a-c] matches any characters except "a", "b" and "c". Write the regular expression that matches any characters except letters, digits and spaces. You must use a negated character set in your expression.


[Examples]

___
txt = " alice15@gmail.com "
pattern = "yourregularexpressionhere"

re.findall(pattern, txt) ➞ ["@", "."]
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and negation in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to write Regular Expressions?
https://www.geeksforgeeks.org/write-regular-expressions/
is a sequence of characters that define a search pattern, mainly for use in pattern matching with strings, or string matching, i.e. “find and replace”-like operations.( …
_________
_________
Regular expression operations
https://docs.python.org/3/library/re.html
Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot be mixed: that …
_________
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________
_________
Regular Expression
https://en.wikipedia.org/wiki/Regular_expression
Is a sequence of characters that specifies a search pattern in text. Usually such patterns are used by string-searching algorithms for "find" or "find and replace" oper …
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________
_________
Python Regular Expression Cheatsheet - Debuggex
https://www.debuggex.com/cheatsheet/regex/python
Regex Cheatsheet
_________
_________
Character Classes or Character Sets
https://www.regular-expressions.info/charclass.html
With a “character class”, also called “character set”, you can tell the regex engine to match only one out of several characters. Simply place the characters you want t …
_________
_________
Online Regex Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________

"""
#Your code should go here:

