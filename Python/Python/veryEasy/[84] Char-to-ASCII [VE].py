"""
##Char-to-ASCII

Create a function that returns the ASCII value of the passed in character.


[Examples]

___
ctoa("A") ➞ 65

ctoa("m") ➞ 109

ctoa("[") ➞ 91

ctoa("\") ➞ 92
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[algorithms] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
ord() Method
https://docs.python.org/3.7/library/functions.html#ord
Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 …
_________
_________
chr() Method
https://docs.python.org/3/library/functions.html?highlight=chr#chr
Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a', while chr(8364) returns the string '€ …
_________
_________
ASCII Table
http://www.asciitable.com
Provides detailed information about the ASCII table for those who are up for a challenge to create their own algorithm.
_________
_________
Python Program to Find ASCII Value of Character
https://www.programiz.com/python-programming/examples/ascii-character
ASCII stands for American Standard Code for Information Interchange. It is a numeric value given to different characters and symbols, for computers to store and manipu …
_________
""" 
# Your code should go here:

valueASCII = lambda input1 : ord(input1)

print(valueASCII("A"))
print(valueASCII("a"))
print(valueASCII("m"))
print(valueASCII("["))
print(valueASCII("\\"))

# The program is complete.