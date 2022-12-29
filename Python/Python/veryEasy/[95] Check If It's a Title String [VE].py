"""
##Check If It's a Title String

Check if a string txt is a title text or not. A title text is one which has all the words in the text start with an upper case letter.


[Examples]

___
check_title("A Mind Boggling Achievement") ➞ True

check_title("A Simple Python Program!") ➞ True

check_title("Water is transparent") ➞ False
_____



[Notes]

N/A


[formatting] [language_fundamentals] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
title() Method
https://www.w3schools.com/python/ref_string_title.asp
Returns a string where the first character in every word is upper case. Like a header, or a title. If the word contains a number or a symbol, the first letter after th …
_________
_________
isupper() Method
https://www.programiz.com/python-programming/methods/string/isupper
Returns whether or not all characters in a string are uppercased or not.
_________
_________
istitle() Method
https://www.w3schools.com/python/ref_string_istitle.asp
Returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
_________
_________
isupper() Method
https://careerkarma.com/blog/python-uppercase/
To check if a string is in uppercase, we can use the isupper() method.
_________
_________
String Title Method
https://www.geeksforgeeks.org/title-in-python/
Is used to convert the first character in each word to uppercase and the remaining characters to lowercase in the string and returns a new string.
_________
_________
all() Method
https://www.programiz.com/python-programming/methods/built-in/all
Returns True when all elements in the given iterable are true. If not, it returns False.
_________
_________
List Comprehension
https://www.programiz.com/python-programming/list-comprehension
Suppose, we want to separate the letters of the word human and add the letters as items of a list. The first thing that comes in mind would be using for loop.
_________
_________
split() Method
https://www.programiz.com/python-programming/methods/string/split
Breaks up a string at the specified separator and returns a list of strings.
_________
_________
ASCII Codes
https://ascii.cl/
Table for easy reference of ASCII characters and symbols, with conversion tables and HTML codes.
_________
""" 
# Your code should go here:

checkTitle = lambda str1 : True if str1 == str1.title() else False

print(checkTitle("A Mind Boggling Achievement"))
print(checkTitle("A Simple Python Program!"))
print(checkTitle("Water is transparent"))
print(checkTitle("nitkarsh"))
print(checkTitle("Nitkarsh"))

# The program is complete.