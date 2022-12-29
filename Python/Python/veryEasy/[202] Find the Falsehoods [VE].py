"""
##Find the Falsehoods

Python will interpret empty values (e.g. 0, (), {}, [], "") as the boolean False. For example, the code "cat" if () else "dog" returns "dog", since () is False.
On the other hand, non-empty values are interpreted as True. For example, "cat" if (3, 2) else "dog" returns "cat" since (3, 2) is True.
Write a function that, given a list of values, returns the list of the values that are False.


[Examples]

___
find_the_falsehoods([0, 1, 2, 3]) ➞ [0]

find_the_falsehoods(["", "a", "ab"]) ➞ [""]

find_the_falsehoods([None, 1, [], [0], 0]) ➞ [None, [], 0]

find_the_falsehoods([]) ➞ []

find_the_falsehoods([[]]) ➞ [[]]

find_the_falsehoods([[[]]]) ➞ []
_____



[Notes]

N/A


[arrays] [language_fundamentals] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Python Test for False list
https://www.geeksforgeeks.org/python-test-for-false-list/
Sometimes, we need to check if a list is completely True of False, these occurrences come more often in testing purposes after the development phase. Hence, having a kn …
_________
_________
Booleans
https://www.w3schools.com/python/python_booleans.asp
In programming you often need to know if an expression is True or False. You can evaluate any expression in Python, and get one of two answers, True or False. When you …
_________
""" 
# Your code should go here:

