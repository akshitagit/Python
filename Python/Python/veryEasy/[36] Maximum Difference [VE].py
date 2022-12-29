"""
##Maximum Difference

Given a list of integers, return the difference between the largest and smallest integers in the list.


[Examples]

___
difference([10, 15, 20, 2, 10, 6]) ➞ 18
# 20 - 2 = 18

difference([-3, 4, -9, -1, -2, 15]) ➞ 24
# 15 - (-9) = 24

difference([4, 17, 12, 2, 10, 2]) ➞ 15
_____



[Notes]

N/A


[arrays] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
max() and min() in Python
https://www.geeksforgeeks.org/max-min-python/
This article brings you a very interesting and lesser known function of Python, namely max() and min(). Now when compared to their C++ counterpart, which only allows tw …
_________
_________
Using Python Lists
http://openbookproject.net/thinkcs/python/english3e/lists.html
A list is an ordered collection of values. The values that make up a list are called its elements, or its items. We will use the term element or item to mean the same t …
_________
_________
Python Lists
https://docs.python.org/3/tutorial/datastructures.html
Python documentation on the List data structure.
_________
""" 
# Your code should go here:

def diffMaxMin(list1):
    return ((max(list1)) - (min(list1)))

print(diffMaxMin([10, 15, 20, 2, 10, 6]))
print(diffMaxMin([-3, 4, -9, -1, -2, 15]))
print(diffMaxMin([4, 17, 12, 2, 10, 2]))

# The program is complete.