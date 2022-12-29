"""
##Balancing Scales

Given a list with an odd number of elements, return whether the scale will tip "left" or "right" based on the sum of the numbers. The scale will tip on the direction of the largest total. If both sides are equal, return "balanced".


[Examples]

___
scale_tip([0, 0, "I", 1, 1]) ➞ "right"
# 0 < 2 so it will tip right

scale_tip([1, 2, 3, "I", 4, 0, 0]) ➞ "left"
# 6 > 4 so it will tip left

scale_tip([5, 5, 5, 0, "I", 10, 2, 2, 1]) ➞ "balanced"
# 15 = 15 so it will stay balanced
_____



[Notes]

___
*) The middle element will always be "I" so you can just ignore it.
*) Assume the numbers all represent the same unit.
*) Both sides will have the same number of elements.
*) There are no such things as negative weights in both real life and the tests!
___



[algorithms] [arrays] [conditions] 



-------------------------------------------------------------------
[Resources]
_________
index( ) Method
https://www.programiz.com/python-programming/methods/list/index
In simple terms, the index() method finds the given element in a list and returns its position.
_________
_________
Understanding Slice Notation
https://stackoverflow.com/questions/509211/understanding-slice-notation
Python supports slice notation for any sequential data type like lists, strings, tuples, bytes, bytearrays, and ranges. Also, any new data structure can add its support …
_________
""" 
# Your code should go here:

