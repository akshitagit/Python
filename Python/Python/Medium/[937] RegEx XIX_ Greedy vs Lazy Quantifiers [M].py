"""
####  RegEx XIX: Greedy vs Lazy Quantifiers  ####

By default quantifiers like * and + are "greedy", meaning that they try to match as many characters as possible. Using ? after the quantifier makes the quantifier "lazy": meaning that it will stop as soon as it finds a match.
___
txt = "1232 2133424 809890 548"
re.findall(".+\s", txt) ➞ ["1232 2133424 809890 "]
re.findall(".+?\s", txt) ➞ ["1232 ", "2133424 ", "809890 "]
_____

Write a regular expression to find all HTML comments in the text. You must use lazy quantifiers in your expression.
___
txt = "... <!-- My -- comment test --> ..  <!----> .. "
pattern = "yourregularexpressionhere"

re.findall(pattern, txt) ➞ ["<!-- My -- comment test -->", "<!---->"]
_____



[Notes]

___
*) HTML comments are formatted <!--this is an HTML comment-->.
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and quantifiers in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[regex] 



-------------------------------------------------------------------
[Resources]
_________
Python Regular Expression Cheatsheet
https://www.debuggex.com/cheatsheet/regex/python
Python RegEx Cheatsheet
_________
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________
_________
Regex Quantifier Tutorial: Greedy, Lazy, Possessive
https://www.rexegg.com/regex-quantifiers.html
Regex Quantifiers Tutorial. Explains the fine details of quantifiers, including greedy, lazy (reluctant) and possessive.
_________

"""
#Your code should go here:

