"""
##Longest Sequence of Consecutive Zeroes

Write a function that returns the longest sequence of consecutive zeroes in a binary string.


[Examples]

___
longest_zero("01100001011000") ➞ "0000"

longest_zero("100100100") ➞ "00"

longest_zero("11111") ➞ ""
_____



[Notes]

If no zeroes exist in the input, return an empty string.


[language_fundamentals] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
split() Method
https://www.geeksforgeeks.org/python-string-split/
Returns a list of strings after breaking the given string by the specified separator.
_________
_________
max() and min() in Python
https://www.geeksforgeeks.org/max-min-python/
This article brings you a very interesting and lesser known function of Python, namely max() and min(). Now when compared to their C++ counterpart, which only allows tw …
_________
_________
Maximum Consecutive One’s (Or Zeros) in a Binary Array
https://www.geeksforgeeks.org/maximum-consecutive-ones-or-zeros-in-a-binary-array/
Given binary array, find count of maximum number of consecutive 1’s present in the array. An efficient solution is traverse array from left to right. If we see a 1, we …
_________
_________
Python's most efficient way to choose longest string in list?
https://stackoverflow.com/questions/873327/pythons-most-efficient-way-to-choose-longest-string-in-list
I have a list of variable length and am trying to find a way to test if the list item currently being evaluated is the longest string contained in the list. And I am us …
_________
_________
How to Sort a List
https://docs.python.org/3/howto/sorting.html
Python lists have a built-in list.sort() method that modifies the list in-place. There is also a sorted() built-in function that builds a new sorted list from an iterab …
_________
""" 
# Your code should go here:

