"""
##X and Y Coordinates

Create a function that converts two lists of x- and y- coordinates into a list of (x, y) coordinates.


[Examples]

___
convert_cartesian([1, 5, 3, 3, 4], [5, 8, 9, 1, 0]) 
➞ [[1, 5], [5, 8], [3, 9], [3, 1], [4, 0]]

convert_cartesian([9, 8, 3], [1, 1, 1]) 
➞ [[9, 1], [8, 1], [3, 1]]
_____



[Notes]

___
*) Each coordinate is a list, not a tuple.
*) x and y arrays will always be the same length.
___



[arrays] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Zip with list output instead of tuple?
https://stackoverflow.com/questions/8372399/zip-with-list-output-instead-of-tuple
What is the fastest and most elegant way of doing list of lists from two lists? I was thinking about using map instead of zip, but I don't know if there is some standar …
_________
_________
List map() Method
https://www.programiz.com/python-programming/methods/built-in/map
Applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
_________
_________
zip() Method
https://www.geeksforgeeks.org/zip-in-python/
To map the similar index of multiple containers so that they can be used just using as single entity.
_________
_________
Lists in Python
https://www.programiz.com/python-programming/list
In this article, we'll learn everything about Python lists; how they are created, slicing of a list, adding or removing elements from them and so on.
_________
_________
zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
Creates an iterator that will aggregate elements from two or more iterables. You can use the resulting iterator to quickly and consistently solve common programming pro …
_________
_________
zip() Method
https://www.programiz.com/python-programming/methods/built-in/zip
The zip() function take iterables (can be zero or more), makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples.
_________
_________
map() Function
https://www.w3schools.com/python/ref_func_map.asp
Executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
_________
""" 
# Your code should go here:

