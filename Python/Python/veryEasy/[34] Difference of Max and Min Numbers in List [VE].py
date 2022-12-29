"""
##Difference of Max and Min Numbers in List

Create a function that takes a list and returns the difference between the biggest and smallest numbers.


[Examples]

___
difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]) ➞ 82
# Smallest number is -50, biggest is 32.

difference_max_min([44, 32, 86, 19]) ➞ 67
# Smallest number is 19, biggest is 86.
_____



[Notes]

N/A


[arrays] [loops] [math] [numbers]



-------------------------------------------------------------------
[Resources]
_________
Aggregations: Min, Max, and Everything In Between
https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html#Minimum-and-Maximum
Python has built-in min and max functions, used to find the minimum value and maximum value of any given array.
_________
_________
list sort() Function
https://www.geeksforgeeks.org/python-list-sort-method/
Can be used to sort a List in ascending, descending, or user-defined order. In each case, the time complexity is O(nlogn) in Python.
_________
_________
Array max() Method
https://www.programiz.com/python-programming/methods/built-in/max
Returns the largest element in an iterable or largest of two or more parameters.
_________
_________
Using the max() and min() Methods
https://www.geeksforgeeks.org/max-min-python/
This article brings you a very interesting and lesser known function of Python, namely max() and min(). Now when compared to their C++ counterpart, which only allows tw …
_________
_________
Array min() Method
https://www.programiz.com/python-programming/methods/built-in/min
Returns the smallest element in an iterable or smallest of two or more parameters.
_________
_________
Python Min and Max Inbuilt Function Example
https://appdividend.com/2019/01/27/python-min-and-max-built-in-function-tutorial-with-example/
Returns the smallest of all input values. Python max() is an inbuilt function that returns the largest of input values.
_________
"""
# Your code should go here:

def diffMaxMin(list1):
    return ((max(list1)) - (min(list1)))

print(diffMaxMin([10, 4, 1, 4, -10, -50, 32, 21]))
print(diffMaxMin([44, 32, 86, 19]))
print(diffMaxMin([1,2,3,4,5,6,7,8,100]))
print(diffMaxMin([-12, -123, -13, -42, -311])) # For negative also the output is positive number.
print(diffMaxMin([-100, 2]))

# The program is complete.
