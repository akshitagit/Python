"""
####  Format VI: Padding  ####

For each challenge of this series you do not need to submit a function. Instead, you need to submit a template string that can formatted in order to get a certain outcome.
Write a three templates string according to the following example. All final strings must have a length of 20 characters:


[Example]

___
starry = "yourtemplatestringhere"
dash = "yourtemplatestringhere"
money = "yourtemplatestringhere"

starry.format("Starry") ➞ "*******Starry*******"
dash.format("Dash") ➞ "----------------Dash"
money.format("Money") ➞ "Money$$$$$$$$$$$$$$$"
_____



[Tips]

You can pad a string with a placeholder in the format {:cdx} where c is the padding character, d is one of three directions (<, ^ or >) and x is the width.
For example:
___
"Best score{:->15}".format('AAA') ➞ "Best score------------AAA"
_____



[Notes]

___
*) Submit a string, not a function.
*) Do not change the name of the variables starry, dash and money.
*) You can find all the exercises in this series over here.
___



[formatting] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String Formatting with str.format() in Python
https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
This tutorial will guide you through some of the common uses of string formatters in Python, which can help make your code and program more readable and user friendly.
_________
_________
format() Method
https://www.programiz.com/python-programming/methods/string/format
Formats the given string into a nicer output in Python.
_________
_________
String format() Method
https://www.programiz.com/python-programming/methods/string/format
Formats the given string into a nicer output in Python.
_________

"""
#Your code should go here:

