"""
####  First and Last Index  ####

Given a word, write a function that returns the first index and the last index of a character.


[Examples]

___
char_index("hello", "l") ➞ [2, 3]
# The first "l" has index 2, the last "l" has index 3.

char_index("circumlocution", "c") ➞ [0, 8]
# The first "c" has index 0, the last "c" has index 8.

char_index("happy", "h") ➞ [0, 0]
# Only one "h" exists, so the first and last index is 0.

char_index("happy", "e") ➞ None
# "e" does not exist in "happy", so we return undefined.
_____



[Notes]

___
*) If the character does not exist in the word, return None.
*) If only one instance of the character exists, the first and last index will be the same.
*) Check the Resources tab for hints.
___



[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
rindex() Method
https://www.programiz.com/python-programming/methods/string/rindex
Returns the highest index of the substring inside the string (if found).
_________
_________
find() Method
https://www.w3schools.com/Python/ref_string_find.asp
The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
_________
_________
Python return Statement
https://www.askpython.com/python/python-return-statement
The python return statement is used in a function to return something to the caller program. We can use the return statement inside a function only. In Python, every fu …
_________
_________
How to loop backwards in Python?
https://stackoverflow.com/questions/3476732/how-to-loop-backwards-in-python
I can think of some ways to do so in python (creating a list of range(1,n+1) and reverse it, using while and --i, ...) but I wondered if there's a more elegant way to d …
_________

"""
#Your code should go here:

