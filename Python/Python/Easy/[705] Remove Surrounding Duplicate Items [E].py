"""
####  Remove Surrounding Duplicate Items  ####

Create a function that takes a sequence of either strings or integers, removes the surrounding duplicates and returns a list of items without any items with the same value next to each other and preserves the original order of items.


[Examples]

___
unique_in_order("AAAABBBCCDAABBB") ➞ ["A", "B", "C", "D", "A", "B"]

unique_in_order("ABBCcAD") ➞ ["A", "B", "C", "c", "A", "D"]

unique_in_order([1, 2, 2, 3, 3]) ➞ [1, 2, 3]
_____



[Notes]

___
*) The initial sequence of items can be either a string or a list.
*) Tests are case sensitive.
___



[formatting] [loops] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
Remove one of two duplicates (next to each other) in a list?
https://stackoverflow.com/questions/49182242/python-remove-one-of-two-duplicates-next-to-each-other-in-a-list
I have a list A= [1, 2, 3, 3, 4, 4, 5, 6, 4, 7] I want to only keep one 3 and 4 if they are next to another identical one. Thus A should become A = [1, 2, 3, 4, 5, 6, 4 …
_________
_________
itertools.groupby()
https://www.geeksforgeeks.org/itertools-groupby-in-python/
Python’s Itertool is a module that provides various functions that work on iterators to produce complex iterators. This module works as a fast, memory-efficient tool th …
_________
_________
Strings
https://developers.google.com/edu/python/strings
Python has a built-in string class named "str" with many handy features (there is an older module named "string" which you should not use). String literals can be enclo …
_________
_________
Enumerate Explained
https://www.afternerd.com/blog/python-enumerate/
In this article, I will teach you everything you should know about Python's enumerate function. Python gives you the luxury of iterating directly over the values of the …
_________
_________
Removing Elements That Have Consecutive Duplicates
https://stackoverflow.com/questions/5738901/removing-elements-that-have-consecutive-duplicates
I was curious about the question: Eliminate consecutive duplicates of list elements, and how it should be implemented in Python. What I came up with is this...
_________

"""
#Your code should go here:

