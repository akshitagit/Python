"""
####  RegEx XI-C: Whitespace Character Class  ####

Write the regular expression that will match a string if there are no spaces right before the last ending punctuation ?. Use the character class \S in your expression.


[Example]

___
txt1 = "Can read a spray chart and a balance sheet. 1 part Executive, 1 part entrepreneur, 2 parts geek and 3 parts baseball coach. Too many parts?"
txt2 = "Can read a spray chart and a balance sheet. 1 part Executive, 1 part entrepreneur, 2 parts geek and 3 parts baseball coach. Too many parts ?"
pattern = "yourregularexpressionhere"

bool(re.search(pattern, txt1)) ➞ True
bool(re.search(pattern, txt2)) ➞ False
_____



[Notes]

___
*) Mark Gallion's Twitter bio is used for educational purposes only.
*) To search for the character ? in RegEx, the pattern must include \?.
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and character classes in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[regex] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Character Classes
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Character_Classes
Character classes distinguish kinds of characters such as, for example, distinguishing between letters and digits.
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________
_________
re.sub(pattern, repl, string, count=0, flags=0)
https://docs.python.org/3/library/re.html#re.sub
Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. If the pattern isn’t found, string is ret …
_________
_________
Online RegEx Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
_________
Python RegEx for a Question Mark
https://stackoverflow.com/questions/54019443/python-regular-expressions-for-a-question-mark
Am working on a data set with a column next review date. This column have missen fields represented by a question mark(?) I want to capture this ? with a regular expres …
_________

"""
#Your code should go here:

