"""
##Concatenating First and Last Character of a String

Create a function that takes a string and returns the concatenated first and last character.


[Examples]

___
first_last("ganesh") ➞ "gh"

first_last("kali") ➞ "ki"

first_last("shiva") ➞ "sa"

first_last("vishnu") ➞ "vu"

first_last("durga") ➞ "da"
_____



[Notes]

There is no empty string.


[language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Get a String Made of the First 2 and the Last 2 Chars from a Given a String
https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-3.php
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty …
_________
_________
How to get first N characters in a string?
https://thispointer.com/python-how-to-get-first-n-characters-in-a-string/
In this article, we will discuss how to fetch/access the first N characters of a string in python. This N can be 1 or 3 etc. Python string is a sequence of characters a …
_________
_________
How would I get the first character from the first string in a list in Python?
https://stackoverflow.com/questions/7108080/python-get-the-first-character-of-the-first-string-in-a-list
You want to end after the first character (character zero), not start after the first character (character zero), which is what the code in your question means.
_________
_________
Check the First or Last Character of a String
https://thispointer.com/check-the-first-or-last-character-of-a-string-in-python/
In this article, we will discuss different ways to check the content of the first or last character of a string in python.
_________
_________
Print the First and Last Letters of a String
https://www.geeksforgeeks.org/print-the-first-and-last-character-of-each-word-in-a-string/
Given a string, the task is to print the first and last character of each word in a string.
_________
_________
Get the Last 4 Characters of a String
https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string
How can I get the last four characters and store them in a string using Python?
_________
_________
Python slice string
https://www.journaldev.com/23584/python-slice-string
Python slice string
_________
""" 
# Your code should go here:

def firstAndLast(str1):
    if (len(str1) >= 2):
        return ("{0}{1}".format(str1[0], str1[-1]))
    else:
        return "Please input str with more than or equal to two characters."
print(firstAndLast("Nitkarsh"))
print(firstAndLast("Anmol"))
print(firstAndLast("Purshotam"))
print(firstAndLast("Varsha"))
print(firstAndLast("NitkarshChourasia"))
print(firstAndLast("AnmolChourasia"))
print(firstAndLast("az"))
print(firstAndLast("a"))
print(firstAndLast(""))

# The program is complete.