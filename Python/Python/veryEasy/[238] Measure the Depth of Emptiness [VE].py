"""
##Measure the Depth of Emptiness

In this challenge you will receive an input of the form:
___
[[[[[[[[[[[]]]]]]]]]]]
_____

In other words, a list containing a list containing a list containing... a list containing nothing.
Your goal is to measure the depth of this list, where [] has a depth 1, [[]] has depth of 2, [[[]]] has depth 3, etc.


[Examples]

___
measure_the_depth([]) ➞ 1

measure_the_depth([[]]) ➞ 2

measure_the_depth([[[]]]) ➞ 3

measure_the_depth([[[[[[[[[[[]]]]]]]]]]]) ➞ 11
_____



[Notes]

One way to solve this is with recursion; but maybe there's a way to "count the brackets"?


[arrays] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
str() Method
https://www.w3schools.com/python/ref_func_str.asp
Converts the specified value into a string.
_________
_________
count() Method
https://www.w3schools.com/python/ref_list_count.asp
Counts the number of occurrences of an element/letter in a list/string.
_________
""" 
# Your code should go here:

