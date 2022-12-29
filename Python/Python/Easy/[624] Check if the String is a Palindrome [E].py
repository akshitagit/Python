"""
####  Check if the String is a Palindrome  ####

A palindrome is a word, phrase, number or other sequence of characters which reads the same backward or forward, such as madam or kayak.
Write a function that takes a string and determines whether it's a palindrome or not. The function should return a boolean (True or False value).


[Examples]

___
is_palindrome("Neuquen") ➞ True

is_palindrome("Not a palindrome") ➞ False

is_palindrome("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!") ➞ True
_____



[Notes]

___
*) Should be case insensitive.
*) Special characters (punctuation or spaces) should be ignored.
___



[strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to reverse a string in Python?
https://stackoverflow.com/questions/931092/reverse-a-string-in-python
There is no built in reverse function for Python's str object. What is the best way of implementing this method? If supplying a very concise answer, please elaborate o …
_________
_________
isalpha() Method
https://docs.python.org/3/library/stdtypes.html?highlight=isalpha#str.isalpha
Return true if all characters in the string are alphabetic and there is at least one character, false otherwise. Alphabetic characters are those characters defined in t …
_________
_________
strip() Method
https://www.tutorialspoint.com/python/string_strip.htm
Returns a copy of the string in which all chars have been stripped from the beginning and the end of the string (default whitespace characters).
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
.span() returns a tuple containing the start-, and end positions of the match. .string returns the string passed into the function .group() returns the part of the st …
_________
_________
Best way to strip punctuation from a string in Python?
https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
From an efficiency perspective, you're not going to beat s.translate(None, string.punctuation) For higher versions of Python use the following code: s.translate(str.m …
_________
_________
String Constants
https://docs.python.org/2/library/string.html
Describes the String library and all of the string constants available so that you do not have to write out long lists of characters.
_________
_________
Remove Punctuations From a String
https://www.programiz.com/python-programming/examples/remove-punctuation
Removes all punctuations from a string. We will check each character of the string using for loop. If the character is a punctuation, empty string is assigned to it.
_________

"""
#Your code should go here:

