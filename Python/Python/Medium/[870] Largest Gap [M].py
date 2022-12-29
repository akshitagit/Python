"""
####  Largest Gap  ####

Given a list of integers, return the largest gap between elements of the sorted version of that list.
Here's an illustrative example. Consider the list:
___
[9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]
_____

... which, after sorting, becomes the list:
___
[0, 0, 4, 5, 5, 6, 9, 20, 25, 26, 26]
_____

... so that we now see that the largest gap in the list is the gap of 11 between 9 and 20.


[Examples]

___
largest_gap([9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]) ➞ 11
# After sorting get [0, 0, 4, 5, 5, 6, 9, 20, 25, 26, 26]
# Largest gap of 11 between 9 and 20

largest_gap([14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]) ➞ 4
# After sorting get [1, 3, 4, 5, 7, 7, 7, 7, 11, 12, 12, 13, 14]
# Largest gap of 4 between 7 and 11

largest_gap([13, 3, 8, 5, 5, 2, 13, 6, 14, 2, 11, 4, 10, 8, 1, 9]) ➞ 2
# After sorting get [1, 2, 2, 3, 4, 5, 5, 6, 8, 8, 9, 10, 11, 13, 13, 14]
# Largest gap of 2 between 6 and 8
_____



[Notes]

N/A


[arrays] [math] [numbers] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
Using the Python zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
In this step-by-step tutorial, you'll learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables i …
_________
_________
max() Function
https://www.programiz.com/python-programming/methods/built-in/max
Returns the largest item in an iterable. It can also be used to find the largest item between two or more parameters.
_________
_________
Finding Differences Between Elements of a List
https://stackoverflow.com/questions/2400840/python-finding-differences-between-elements-of-a-list
Finding differences between elements of a list.
_________
_________
sorted() Function
https://www.w3schools.com/python/ref_func_sorted.asp#:~:text=Python%20sorted%20%28%29%20Function%201%20Definition%20and%20Usage.,ascending%2C%20True%20will%20sort%20descending.%204%20More%20Examples
Returns a sorted list of the specified iterable object. You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numeri …
_________
_________
Calculate Difference Between Adjacent Items in a List
https://stackoverflow.com/questions/7172933/calculate-difference-between-adjacent-items-in-a-python-list
I have a list of millions of numbers. I want to find out if the difference between each number in the ordered list is the same for the entire list.
_________

"""
#Your code should go here:

