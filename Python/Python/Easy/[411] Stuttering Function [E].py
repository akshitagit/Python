"""
##Stuttering Function

Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ...
and space after each, and then the word is pronounced with a question mark ?.


[Examples]

___
stutter("incredible") ➞ "in... in... incredible?"

stutter("enthusiastic") ➞ "en... en... enthusiastic?"

stutter("outstanding") ➞ "ou... ou... outstanding?"
_____



[Notes]

Assume all input is in lower case and at least two characters long.


[algorithms] [formatting] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to get the first 2 letters of a string in Python?
https://stackoverflow.com/questions/20988835/how-to-get-the-first-2-letters-of-a-string-in-python/20989153
How to get the first 2 letters of a string in Python? def first2(s): return s[:2]
_________
_________
Format Specification Mini-Language
https://docs.python.org/3.5/library/string.html#format-specification-mini-language
Are used within replacement fields contained within a format string to define how individual values are presented (see Format String Syntax). They can also be passed di …
_________
_________
Lists
https://docs.python.org/3.3/tutorial/introduction.html#lists
Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated val …
_________
_________
Python Strings
https://www.w3schools.com/python/python_strings.asp
Are surrounded by either single quotation marks, or double quotation marks. 'hello' is the same as "hello". You can display a string literal with the print() function.
_________
_________
String Formatting Best Practices
https://realpython.com/python-string-formatting/
Learn the four main approaches to string formatting in Python, as well as their strengths and weaknesses. You'll also get a simple rule of thumb for how to pick the bes …
_________
_________
String Format Cookbook
https://mkaz.blog/code/python-string-format-cookbook/
Python v2.7 introduced a new string fomatting method, that is now the default in Python3. I started this string formatting cookbook as a quick reference to help me form …
_________
""" 
# Your code should go here:

def stutter(str1):
    if len(str1) >= 2:
        return "{0}... {1}... {2}?".format(str1[:2].lower(), str1[:2].lower(), str1.lower())
    else:
        return "String length should be at least two characters long."

print(stutter("incredible"))
print(stutter("enthusiastic"))
print(stutter("outstanding"))
print(stutter("NItKArsh"))
print(stutter("a"))

# The program is complete.