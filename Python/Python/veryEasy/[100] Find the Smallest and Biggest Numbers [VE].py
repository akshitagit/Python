"""
##Find the Smallest and Biggest Numbers

Create a function that accepts a list of numbers and return both the minimum and maximum numbers, in that order (as a list).


[Examples]

___
min_max([1, 2, 3, 4, 5]) ➞ [1, 5]

min_max([2334454, 5]) ➞ [5, 2334454]

min_max([1]) ➞ [1, 1]
_____



[Notes]

All test lists will have at least one element and are valid.


[arrays] [language_fundamentals] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
min() Method
https://www.programiz.com/python-programming/methods/built-in/min
Returns the smallest element in an iterable or smallest of two or more parameters.
_________
_________
max() Method
https://www.programiz.com/python-programming/methods/built-in/max
Returns the largest element in an iterable or largest of two or more parameters.
_________
_________
Find the Largest and Smallest Number in a List
https://medium.com/programminginpython-com/python-program-to-find-the-largest-and-smallest-number-in-a-list-fd8fac8aba08
Hello everybody, this is a Python program which finds out the smallest and largest number in the list. Here we use 2 predefined functions min() and max() which check fo …
_________
_________
min() and max()
https://www.tutorialspoint.com/use-of-min-and-max-in-python
In this article, we will be learning about min and max functions included in the Python Standard Library. It accepts infinite no of parameters according to the usage
_________
_________
Python Slice First and Last Element in List
https://stackoverflow.com/questions/12218796/python-slice-first-and-last-element-in-list
Is there a way to slice only the first and last item in a list? For example; If this is my list: >>> some_list ['1', 'B', '3', 'D', '5', 'F'] I want to do this (obvio …
_________
_________
Finding Magnitude or Length of a Vector
https://www.youtube.com/watch?v=6GoMXuE1FOw
I give the formula, and do a couple examples of finding the magitude, or length, or a vector.
_________
_________
count() Method
https://www.programiz.com/python-programming/methods/list/count
Returns the number of occurrences of an element in a list.
_________
_________
Python Arrays
https://www.w3schools.com/python/python_arrays.asp
Arrays are used to store multiple values in one single variable.
_________
""" 
# Your code should go here:

def minMax(list1):
    if len(list1) > 0:
        return [min(list1), max(list1)]
    else:
        return "The list must have at least one element."

minMax1 = lambda list1 : list((min(list1), max(list1))) if len(list1) > 0 else "The list must have at least one element."

print(minMax([1, 2, 3, 4, 5]))
print(minMax1([1, 2, 3, 4, 5]))
print(minMax([2334454, 5]))
print(minMax1([2334454, 5]))
print(minMax([1]))
print(minMax1([1]))
print(minMax([0]))
print(minMax1([0]))
print(minMax([]))
print(minMax1([]))

# The program is complete.