"""
##Which One Is Your Type?

Python has three main types of data structures formed by smaller objects:
___
*) Lists, written with [] square brackets, such as [1, 2, 4, 8].
*) Tuples, written with () parentheses, such as (7, 8, 9).
*) Sets, written with{} curly brackets, such as {2, 3, 5, 7, 11, 13}.
___

Each of these types has its own special properties and peculiarities that are worth knowing, but this challenge is only about transforming these data types into each other.
This can be done as in the following:
___
*) tuple([1,2,4,8]) returns (1,2,4,8)
*) list({2,3,5,7,11}) returns [2, 3, 5, 7, 11, 13]
*) set((1,2,4)) returns {1,2,4}
___

Given two data structures, data1 and data2, return data2 converted to the type of data1.


[Examples]

___
convert([1, 2, 4, 8], (7, 8, 9)) ➞ [7, 8, 9]

convert((7, 8, 9), [1, 2, 4, 8]) ➞ (1, 2, 4, 8)

convert([1, 2, 4, 8], {2, 3, 5, 7, 11, 13}) ➞ [2, 3, 5, 7, 11, 13]

convert({2, 3, 5, 7, 11, 13}, [1, 2, 4, 8]) ➞ {8, 1, 2, 4}
_____



[Notes]

___
*) You might have noticed that the last example gives {8, 1, 2, 4} rather than{1, 2, 4, 8}. This has to do with the fact that in sets order doesn't matter, so that Python considers {8, 1, 2, 4} and {1, 2, 4, 8} to be the same set.
*) In the test cases you won't have to worry about orders: the answers will always have the order given by applying the list(), tuple(), set() functions.
___



[arrays] [data_structures] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Data Types
https://www.w3schools.com/python/python_datatypes.asp
An introduction to data types and how to convert between them.
_________
_________
type() Method
https://www.w3schools.com/python/ref_func_type.asp
Returns the type of the specified object.
_________
_________
Convert a List into a Tuple
https://www.geeksforgeeks.org/python-convert-a-list-into-a-tuple/#:~:text=Typecasting%20to%20tuple%20can%20be,simply%20using%20tuple(list_name).&text=Approach%20%232%20%3A,a%20loop%20inside%20tuple()%20.&text=This%20essentially%20unpacks%20the%20list,the%20single%20comma%20(%2C%20).
Given a list, write a Python program to convert the given list into a tuple.
_________
_________
isinstance() Method
https://www.w3schools.com/python/ref_func_isinstance.asp
Returns True if the object passed to it is of the specified type else False
_________
""" 
# Your code should go here:

