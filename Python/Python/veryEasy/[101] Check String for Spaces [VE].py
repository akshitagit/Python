"""
##Check String for Spaces

Create a function that returns True if a string contains any spaces.


[Examples]

___
has_spaces("hello") ➞ False

has_spaces("hello, world") ➞ True

has_spaces(" ") ➞ True

has_spaces("") ➞ False

has_spaces(",./!@#") ➞ False
_____



[Notes]

___
*) An empty string does not contain any spaces.
*) Try doing this without RegEx.
___



[strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to check if space is in a string?
https://stackoverflow.com/questions/3301395/check-if-space-is-in-a-string
I'm writing a program that checks whether the string is a single word. Why doesn't this work and is there any better way to check if a string has no spaces/is a single …
_________
_________
Checking whitespace in a string?
https://stackoverflow.com/questions/26987222/checking-whitespace-in-a-string-python/26987329
Why do I always get YES!!!? I need to return NO!!! if the string contain a whitespace (newline, tap, space)
_________
_________
count() Method
https://www.w3schools.com/python/ref_list_count.asp
Returns an integer of how many times something is repeated.
_________
_________
Python RegEx (With Examples)
https://www.programiz.com/python-programming/regex
In this tutorial, you will learn about regular expressions (RegEx), and use Python's re module to work with RegEx (with the help of examples).
_________
_________
isspace() Method
https://www.javatpoint.com/python-string-isspace-method
Used to check space in the string. It returns true if there are only whitespace characters in the string. Otherwise it returns false. Space, newline, and tabs etc are k …
_________
""" 
# Your code should go here:

def containSpaces(str1):
    if " " in str1:
        return True
    else:
        return False

contSpaceLambda = lambda str1 : True if " " in str1 else False

def spaceCountMethod(str1):
    if str1.count(" ") <= 0:
        return False
    else:
        return True

spaceCountMethodLambda = lambda str1 : False if str1.count(" ") <= 0 else True

# import re

# def regContSpace(str1): # Learn to use RegEx Well.
#     if re.match([ ], str1) == True:
#         return True
#     else:
#         return False

print(containSpaces("Hello"))
print(containSpaces("Hello World!"))
print(containSpaces(""))
print(contSpaceLambda("Hello"))
print(contSpaceLambda("Hello World!"))
print(contSpaceLambda(""))
print(spaceCountMethod("Hello"))
print(spaceCountMethod("Hello World"))
print(spaceCountMethod(""))
print(spaceCountMethodLambda("Hello"))
print(spaceCountMethodLambda("Hello World"))
print(spaceCountMethodLambda(""))
# print(regContSpace("Hello!"))
# print(regContSpace("Hello World!"))
# print(regContSpace(""))

# The program is complete.