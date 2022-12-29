"""
##RegEx XV: Alternation

The vertical bar | is the equivalent to "or" in RegEx. The regular expression x|y matches either "x" or "y". Write the regular expression that will match all red flag and blue flag in a string. You must use | in your expression. Flags can come in any order.


[Examples]

___
txt1 = "red flag blue flag"
txt2 = "yellow flag red flag blue flag green flag"
txt3 = "pink flag red flag black flag blue flag green flag red flag"
pattern = "yourregularexpressionhere"

re.findall(pattern, txt1) ➞ ["red flag", "blue flag"]
re.findall(pattern, txt2) ➞ ["red flag", "blue flag"]
re.findall(pattern, txt3) ➞ ["red flag", "blue flag", "red flag"]
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and alternation in the Resources tab.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[formatting] [regex] 



-------------------------------------------------------------------
[Resources]
_________
Online Regex Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________
_________
Alternation with The Vertical Bar or Pipe Symbol
https://www.regular-expressions.info/alternation.html
I already explained how you can use character classes to match a single character out of several possible characters. Alternation is similar. You can use alternation to …
_________
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________
_________
Python Regular Expression Cheatsheet
https://www.debuggex.com/cheatsheet/regex/python
Regex Cheatsheet
_________
""" 
# Your code should go here:

