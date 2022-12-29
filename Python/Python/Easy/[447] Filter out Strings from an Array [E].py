"""
##Filter out Strings from an Array

Create a function that takes a list of non-negative integers and strings and return a new list without the strings.


[Examples]

___
filter_list([1, 2, "a", "b"]) ➞ [1, 2]

filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]

filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
_____



[Notes]

___
*) Zero is a non-negative integer.
*) The given list only has integers and strings.
*) Numbers in the list should not repeat.
*) The original order must be maintained.
___



[arrays] [formatting] [loops] 



-------------------------------------------------------------------
[Resources]
_________
isinstance() Method
https://www.programiz.com/python-programming/methods/built-in/isinstance
The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).
_________
_________
What are the differences between type() and isinstance()?
http://stackoverflow.com/questions/1549801/differences-between-isinstance-and-type-in-python
To summarize the contents of other (already good!) answers, isinstance caters for inheritance (an instance of a derived class is an instance of a base class, too), whil …
_________
_________
isinstance() Method
https://docs.python.org/3/library/functions.html#isinstance
Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the g …
_________
_________
Map, Filter and Reduce
http://book.pythontips.com/en/latest/map_filter.html
These are three functions which facilitate a functional approach to programming. We will discuss them one by one and understand their use cases.
_________
_________
Filter a list in python get integers
https://stackoverflow.com/questions/4357832/filter-a-list-in-python-get-integers
Filter a list in python get integers
_________
_________
type() Method
https://www.geeksforgeeks.org/python-type-function/
Returns class type of the argument(object) passed as parameter.
_________
_________
List Comprehension
https://www.programiz.com/python-programming/list-comprehension
In this article, we will learn about Python list comprehensions, and how to use it.
_________
_________
How to check if type of a variable is string?
https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
Helps check if the contents in the list are a certain datatype. In this case the method will check if the variable is of data type string or not
_________
_________
Python Lists
https://developers.google.com/edu/python/lists
Python has a great built-in list type named "list". List literals are written within square brackets [ ]. Lists work similarly to strings -- use the len() function and …
_________
""" 
# Your code should go here:

