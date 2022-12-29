"""
##Snail Race

Steve and Maurice have racing snails. They each have three, a slow s, medium m and fast f one. Although Steve's snails are all a bit stronger than Maurice's, Maurice has a trick up his sleeve. His plan is:

Create a function that determines whether Maurice's plan will work by outputting True if Maurice wins 2/3 games.
The function inputs:



[Examples]

___
maurice_wins([3, 5, 10], [4, 7, 11]) ➞ True
# Since the matches are (3, 11), (5, 4) and (10, 7), Maurice wins 2 out of 3.

maurice_wins([6, 8, 9], [7, 12, 14]) ➞ False
# Since the matches are (6, 14), (8, 7) and (9, 12), Steve wins 2 out of 3.

maurice_wins([1, 8, 20], [2, 9, 100]) ➞ True
_____



[Notes]

___
*) Maurice wins if his competing snail's speed strictly exceeds Steve's snail's speed.
*) Steve will always play in this order: [f, s, m].
*) The order you'll get the snails is always in ascending order.
___



[arrays] [games] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Multiple Assignment and Tuple Unpacking Improve Code Readability
https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
In this article we’ll see what multiple assignment is, we’ll take a look at common uses of multiple assignment, and then we’ll look at a few uses for multiple assignmen …
_________
_________
zip() Method
https://www.programiz.com/python-programming/methods/built-in/zip
Take iterables (can be zero or more), makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples.
_________
""" 
# Your code should go here:

