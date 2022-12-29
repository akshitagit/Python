"""
##RegEx XVIII: Fixed Quantifiers

Fixed quantifiers indicate numbers of characters or expressions to match.
x{n} matches exactly "n" occurrences of the preceding item "x":
___
re.findall("a{2}", "candy") ➞ []
re.findall("a{2}", "caandy") ➞ ["aa"]
_____

x{n,} matches at least "n" occurrences of the preceding item "x":
___
re.findall("a{2,}", "candy") ➞ []
re.findall("a{2,}", "caandy") ➞ ["aa"]
re.findall("a{2,}", "caaaaandy") ➞ ["aaaaa"]
_____

x{n,m} matches at least "n" and at most "m" occurrences of the preceding item "x":
___
re.findall("a{1,3}", "cndy") ➞ []
re.findall("a{1,3}", "candy") ➞ ["a"]
re.findall("a{1,3}", "caandy") ➞ ["aa"]
re.findall("a{1,3}", "caaaaandy") ➞ ["aaa"]
_____

Write the regular expression to find the ellipsis (3 or more dots in a row) in a string. You must use one of the 3 fixed quantifiers above in your expression.


[Example]

___
txt = "Hello!... Wait. How goes?..... GoodBye!.."
pattern = "yourregularexpressionhere"
re.findall(pattern, txt) ➞ ["...", "....."]
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and quantifiers in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[regex] 



-------------------------------------------------------------------
[Resources]
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________
_________
Python Regex: re.match(), re.search(), re.findall()
https://www.guru99.com/python-regular-expressions-complete-tutorial.html
A regular expression or regex is a special text string used for describing a search pattern. Learn re module, re.match(),re.search(), re.findall(), re.split() methods i …
_________
_________
Regex
https://www.w3schools.com/python/python_regex.asp
.span() returns a tuple containing the start-, and end positions of the match. .string returns the string passed into the function .group() returns the part of the stri …
_________
_________
Ellipsis
https://www.grammarly.com/blog/ellipsis/
Are three periods in row that show that something has been left out. Learn how to properly use to impove your writing today.
_________
_________
Python Regular Expression Cheatsheet
https://www.debuggex.com/cheatsheet/regex/python
RegEx Cheatsheet
_________
_________
Online RegEx Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________
_________
Regular Expressions Reference: Quantifiers
https://www.regular-expressions.info/refrepeat.html
JGsoft .NET Java Perl PCRE PCRE2 PHP Delphi R JavaScript VBScript XRegExp Python Ruby std::regex Boost Tcl ARE POSIX BRE POSIX ERE GNU BRE GNU ERE …
_________
""" 
# Your code should go here:

