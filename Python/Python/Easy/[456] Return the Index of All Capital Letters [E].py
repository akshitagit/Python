"""
##Return the Index of All Capital Letters

Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.


[Examples]

___
index_of_caps("eDaBiT") ➞ [1, 3, 5]

index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]

index_of_caps("determine") ➞ []

index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]

index_of_caps("sUn") ➞ [1]
_____



[Notes]

___
*) Return an empty list if no uppercase letters are found in the string.
*) Special characters ($#@%) and numbers will be included in some test cases.
*) Assume all words do not have duplicate letters.
___



[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
isupper(), islower(), lower(), upper() in Python and their applications
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
In Python, isupper() is a built-in method used for string handling. The isupper() methods returns “True” if all characters in the string are uppercase, Otherwise, It re …
_________
_________
index() Method
https://www.programiz.com/python-programming/methods/list/index
Searches an element in the list and returns its index.
_________
_________
enumerate() Method
https://docs.python.org/3/library/functions.html#enumerate
Returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.
_________
_________
Python Enumerate
https://www.youtube.com/watch?v=pfkiDIKRrkU
Tutorial about the python enumerate() function. I show you how to use enumerate in a for loop, I explain how it works. The enumerate function provides a counter for an …
_________
_________
List Comprehension
https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
An elegant implementation of creating a new list based on certain conditions prescribed on an old list
_________
_________
Enumerate
http://book.pythontips.com/en/latest/enumerate.html
Enumerate is a built-in function of Python. Its usefulness can not be summarized in a single line. Yet most of the newcomers and even some advanced programmers are unaw …
_________
_________
Finding the index of an item given a list containing it in Python?
http://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python
For a list ["foo", "bar", "baz"] and an item in the list "bar", how do I get its index (1) in Python?
_________
_________
Get the Indices of Capital Letters in a String
https://stackoverflow.com/questions/28402480/get-the-indices-of-capital-letters-in-a-string
How can I get a list with the indices of where a capital letter is, so I can make the letters at that same spot in the new string uppercase?
_________
_________
Check if any character of a string is uppercase Python?
http://stackoverflow.com/questions/33883512/check-if-any-character-of-a-string-is-uppercase-python
Say I have a string word. This string can change what characters it contains. e.g. word = "UPPER£CASe" How would I test the string to see if any character in the str …
_________
""" 
# Your code should go here:

