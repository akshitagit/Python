"""
##Front 3 - Slice Check Repeat Concatenate

Create a function that takes a string; we'll say that the front is the first three characters of the string.
If the string length is less than three characters, the front is whatever is there. Return a new string, which is three copies of the front.


[Examples]

___
front3("Python") ➞ "PytPytPyt"

front3("Cucumber") ➞ "CucCucCuc"

front3("bioshock") ➞ "biobiobio"
_____



[Notes]

Don't forget to return the result.


[conditions] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Slice String
https://www.journaldev.com/23584/python-slice-string
Supports slicing to create substring. Note that Python string is immutable, slicing creates a new substring from the source string and original string remains unchanged.
_________
_________
String Length Function
https://www.w3schools.com/python/gloss_python_string_length.asp
Returns the length of a string.
_________
_________
Python Slice Strings
https://www.w3schools.com/python/gloss_python_string_slice.asp
You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
_________
_________
How to Concatenate and Slice Lists
https://datatofish.com/concatenate-slice-lists-python/
How to concatenate and slice lists in Python. I'll review few examples to illustrate these concepts.
_________
_________
String Slicing
https://www.geeksforgeeks.org/string-slicing-in-python/?ref=gcse
Is about obtaining a sub-string from the given string by slicing it respectively from start to end. Python slicing can be done in two ways.
_________
""" 
# Your code should go here:

def start3(str1):
    return str1[:3] * 3

print(start3("Nitkarsh"))
print(start3("Anmol"))
print(start3("Purshotam"))
print(start3("Hey"))
print(start3("A"))
print(start3(""))

# The program is complete.