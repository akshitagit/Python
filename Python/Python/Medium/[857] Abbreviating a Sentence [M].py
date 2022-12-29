"""
####  Abbreviating a Sentence  ####

Create a function which takes a sentence and returns its abbreviation. Get all of the words over or equal to n characters in length and return the first letter of each, capitalised and overall returned as a single string.


[Examples]

___
abbreviate("do it yourself") ➞ "Y"

abbreviate("do it yourself", 2) ➞ "DIY"
# "do" and "it" are included because the second parameter specified that word lengths 2 are allowed.

abbreviate("attention AND deficit OR hyperactivity THE disorder") ➞ "ADHD"
# Words below the default 4 characters are not included in the abbreviation.

abbreviate("the acronym of long word lengths", 5) ➞ "AL"
# "acronym" and "lengths" have 5 or more characters.
_____



[Notes]

There may not be an argument given for n so set the default to 4.


[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
split() Method
https://www.geeksforgeeks.org/python-string-split/
Returns a list of strings from a given string broken based on the separator.
_________
_________
isupper(), islower(), lower(), upper()
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
isupper() is a built-in method used for string handling. The isupper() methods returns “True” if all characters in the string are uppercase, Otherwise, It returns “Fals …
_________
_________
Default Arguments
https://www.tutorialspoint.com/What-are-default-arguments-in-python
Sets a default parameter if a value isn't set for that parameter.
_________
_________
Default Parameter Value
https://www.w3schools.com/python/gloss_python_function_default_parameter.asp
The following example shows how to use a default parameter value. If we call the function without argument, it uses the default value...
_________

"""
#Your code should go here:

