"""
####  The Karaca's Encryption Algorithm  ####

Make a function that encrypts a given input with these steps:
Input: "apple"
Step 1: Reverse the input: "elppa"
Step 2: Replace all vowels using the following chart:
___
a => 0
e => 1
i => 2
o => 2
u => 3

# "1lpp0"
_____

Step 3: Add "aca" to the end of the word: "1lpp0aca"
Output: "1lpp0aca"


[Examples]

___
encrypt("banana") ➞ "0n0n0baca"

encrypt("karaca") ➞ "0c0r0kaca"

encrypt("burak") ➞ "k0r3baca"

encrypt("alpaca") ➞ "0c0pl0aca"
_____



[Notes]

All inputs are strings, no uppercases and all output must be strings.


[algorithms] [cryptography] [formatting] [regex] 



-------------------------------------------------------------------
[Resources]
_________
maketrans() with one argument
https://www.journaldev.com/23697/python-string-translate#maketrans-with-one-argument
We can create a translation table using maketrans() function or provide it manually using a dictionary mapping. We can pass maximum three string arguments to maketrans( …
_________
_________
replace() Method
https://www.programiz.com/python-programming/methods/string/replace
Returns a copy of the string where all occurrences of a substring is replaced with another substring.
_________
_________
Python Reverse String
https://www.journaldev.com/23647/python-reverse-string
Python String doesn’t have a built-in reverse() function. However, there are various ways to reverse a string in Python. Some of the common ways to reverse a string are ...
_________
_________
Karaca’s Encryption
https://amenoren.medium.com/karacas-encryption-python-99a854bd8c8b
Blog reviewing this challenge and methods to solve.
_________
_________
Convert List to Dictionary
https://careerkarma.com/blog/python-convert-list-to-dictionary/
Learn how to convert a list to a dictionary using dictionary comprehension, the dict.fromkeys() method, and the zip() function.
_________
_________
List Comprehension Using If-else
https://pythonguides.com/python-list-comprehension-using-if-else/
Keep reading to know more on Python list comprehension using if-else. Python list comprehension using if without else and nestedif statement.
_________
_________
Join() String Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable (list, string, tuple), separated by a string separator.
_________
_________
Dict-based Find and Replace Deluxe
http://pythoninthewyld.com/2018/03/12/dict-based-find-and-replace-deluxe/
We're going to go through several examples of find-and-replace tasks of varying complexity. We'll also find some potential hiccups and how to avoid them. We're going to …
_________
_________
How do you change one character in a string in Python?
https://www.quora.com/How-do-you-change-one-character-in-a-string-in-Python
Putting everyone’s answers into one function… def change_char(s, p, r): return s[:p]+r+s[p+1:] Call the function like this: s is the original string, p is the posi …
_________

"""
#Your code should go here:

