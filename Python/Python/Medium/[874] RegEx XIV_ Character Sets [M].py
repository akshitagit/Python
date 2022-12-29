"""
####  RegEx XIV: Character Sets  ####

A Character Set will match any characters within a pair of brackets [ ]. You can specify a range of characters by using a hyphen.
___
[abcd] == [a-d]
_____

If the hyphen appears as the first or last character then it is considered a literal hyphen.
___
txt = "non-profit"
pattern = "[abc-]"

re.findall(pattern, txt) ➞ ["-"]
_____

You can also use character classes in a character set.
___
[a-zA-Z0-9_] == [\w]
_____

Write the regular expression that will match an "x" followed by two hexadecimal digits. A hexadecimal digit can be either one of the 10 decimal digits (0 to 9) or a letter from A to F.


[Examples]

___
txt1 = "Exception 0xAF"
txt2 = "Exception 0xD3"
txt3 = "Exception 0xd3"
txt4 = "Exception 0xZZ"
pattern = "yourregularexpressionhere"

re.findall(pattern, txt1) ➞ ["xAF"]
re.findall(pattern, txt2) ➞ ["xD3"]
re.findall(pattern, txt3) ➞ []
re.findall(pattern, txt4) ➞ []
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and character sets in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[regex] 



-------------------------------------------------------------------
[Resources]
_________
Python Regular Expression Cheatsheet
https://www.debuggex.com/cheatsheet/regex/python
Regex Cheatsheet
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________
_________
Online RegEx Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
_________
Character Classes or Character Sets
https://www.regular-expressions.info/charclass.html
With a “character class”, also called “character set”, you can tell the regex engine to match only one out of several characters. Simply place the characters you want t …
_________

"""
#Your code should go here:

