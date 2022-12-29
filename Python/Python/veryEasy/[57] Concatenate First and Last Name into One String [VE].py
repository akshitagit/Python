"""
##Concatenate First and Last Name into One String

Given two strings, first_name and last_name, return a single string in the format "last, first".


[Examples]

___
concat_name("First", "Last") ➞ "Last, First"

concat_name("John", "Doe") ➞ "Doe, John"

concat_name("Mary", "Jane") ➞ "Jane, Mary"
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[formatting] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Splitting, Concatenating, and Joining Strings in Python
https://realpython.com/python-string-split-concatenate-join/
In this article, you will learn some of the most fundamental string operations: splitting, concatenating, and joining. Not only will you learn how to use these tools, b …
_________
_________
String Formatting
https://realpython.com/python-string-formatting/
Learn the four main approaches to string formatting in Python, as well as their strengths and weaknesses. You'll also get a simple rule of thumb for how to pick the bes …
_________
_________
String Concatenation
https://www.w3schools.com/python/gloss_python_string_concatenation.asp
Means add strings together. Use the + character to add a variable to another variable.
_________
_________
format() Function
https://www.educba.com/python-format-function/
Guide to Python format() Function. Here we discuss the Introduction to Python format() Function along with different examples.
_________
_________
Calculate Age in Days
https://stackoverflow.com/questions/48693017/calculate-age-in-days-with-python
Calculate age in days with python.
_________
_________
Python For Loops
https://www.w3schools.com/python/python_for_loops.asp
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
_________
_________
sign up
https://edabit.com/challenges/javascript
sign up
_________
_________
Using % and .format() for Great Good
https://pyformat.info/
Python has had awesome string formatters for many years but the documentation on them is far too theoretic and technical. With this site we try to show you the most com …
_________
""" 
# Your code should go here:

def concatName(fname, lname):
    return ("{1}, {0}".format(fname,lname))

print(concatName("First", "Last"))
print(concatName("Nitkarsh", "Chourasia"))
print(concatName("Anmol", "Chourasia"))
print(concatName("Purshotam", "Bohra"))

# The program is complete.