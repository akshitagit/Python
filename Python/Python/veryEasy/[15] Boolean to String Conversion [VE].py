"""
##Boolean to String Conversion

Create a function that takes a boolean variable flag and returns it as a string.


[Examples]

___
bool_to_string(True) ➞ "True"

bool_to_string(False) ➞ "False"
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[bit_operations] [conditions] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
str() Method
https://www.w3schools.com/python/ref_func_str.asp
Converts the specified value into a string.
_________
_________
Python Booleans
https://www.w3schools.com/python/python_booleans.asp
Booleans represent one of two values: True or False.
_________
_________
Python Strings
https://www.w3schools.com/python/python_strings.asp
Strings in python are surrounded by either single quotation marks, or double quotation marks. 'hello' is the same as "hello".
_________
_________
Python Data Types
https://www.w3schools.com/python/python_datatypes.asp
In programming, data type is an important concept. Variables can store data of different types, and different types can do different things.
_________
_________
Video Walking Through the Challenge
https://www.youtube.com/watch?v=DgfGNztJUkw
In this video, you will learn how to solve these problems in Python: Intro of Edabit, Pair Management, Boolean to String Conversion, Broken Bridge...
_________
""" 
# Your code should go here:

def boolToStr(bool):
    return (str(bool))

print(boolToStr(True))
print(boolToStr(False))
print(type(boolToStr(True)))
print(type(boolToStr(False)))

# The program is complete.