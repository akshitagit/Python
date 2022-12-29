"""
##Typing Game

You're in the midst of creating a typing game.
Create a function that takes in two lists: the list of user-typed words, and the list of correctly-typed words and outputs a list containing 1s (correctly-typed words) and -1s (incorrectly-typed words).
___
# Inputs:
User-typed: ["cat", "blue", "skt", "umbrells", "paddy"]
Correct: ["cat", "blue", "sky", "umbrella", "paddy"]

# Output: [1, 1, -1, -1, 1]
_____



[Examples]

___
correct_stream(
  ["it", "is", "find"],
  ["it", "is", "fine"]
) ➞ [1, 1, -1]

correct_stream(
  ["april", "showrs", "bring", "may", "flowers"],
  ["april", "showers", "bring", "may", "flowers"]
) ➞ [1, -1, 1, 1, 1]
_____



[Notes]

The input list lengths will always be the same.


[arrays] [games] [loops] 



-------------------------------------------------------------------
[Resources]
_________
zip() Method
https://www.geeksforgeeks.org/zip-in-python/
Map the similar index of multiple containers so that they can be used just using as single entity.
_________
_________
List Comprehension in Python
https://hackernoon.com/list-comprehension-in-python-8895a785550b
List comprehensions are used for creating a new list from other iterables.
_________
_________
Comparing same index in 2 lists?
https://stackoverflow.com/questions/38035317/comparing-same-index-in-2-lists
Is there a way to find if the same indexes on 2 lists are the same? For example: x_list = [1, 2, 3, 4, 5] y_list = [1, 2, A, B, 5] I want to know whether the first in …
_________
_________
zip() Method
https://www.programiz.com/python-programming/methods/built-in/zip
The zip() function take iterables (can be zero or more), makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples.
_________
""" 
# Your code should go here:

