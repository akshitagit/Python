"""
##List From a Range of Numbers

Create a function that returns a list of all the integers between two given numbers start and end.


[Examples]

___
range_of_num(2, 4) ➞ [3]

range_of_num(5, 9) ➞ [6, 7, 8]

range_of_num(2, 11) ➞ [3, 4, 5, 6, 7, 8, 9, 10]
_____



[Notes]

___
*) start will always be <= end.
*) start and end are NOT included in the final list.
*) If start == end, return an empty list.
___



[arrays] [language_fundamentals] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
range() Function
https://www.w3schools.com/python/ref_func_range.asp
Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
_________
_________
list() Constructor
https://www.programiz.com/python-programming/methods/built-in/list
Returns a list in Python. In this tutorial, we will learn to use list() in detail with the help of examples.
_________
_________
append() Function
https://thispointer.com/python-how-to-create-an-empty-list-and-append-items-to-it/#:~:text=In%20Python%2C%20an%20empty%20list,returns%20an%20empty%20list%20i.e.
How to store items in an empty list.
_________
_________
Range to a List
https://www.geeksforgeeks.org/range-to-a-list-in-python/
Returns a list from a range in python. Often times we want to create a list containing a continuous value like, in a range of 100-200. Let’s discuss how to create a lis …
_________
""" 
# Your code should go here:

numRange = lambda start , end : list(range(start+1, end)) if start <= end else [] if start == end else "Please specify proper inputs."  # Yeah, maybe readability is being sacrificed, maybe.

print(numRange(2, 4))
print(numRange(5, 9))
print(numRange(2, 11))
print(numRange(9, 9))
print(numRange(3, 3))
print((numRange(10, 3)))

# The program is complete.