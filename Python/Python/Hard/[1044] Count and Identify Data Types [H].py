"""
####  Count and Identify Data Types  ####

Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.
List order is:
___
[int, str, bool, list, tuple, dictionary]
_____



[Examples]

___
count_datatypes(1, 45, "Hi", False) ➞ [2, 1, 1, 0, 0, 0]

count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) ➞ [3, 0, 0, 1, 1, 0]

count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) ➞ [2, 2, 3, 1, 0, 2]

count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) ➞ [2, 0, 1, 2, 2, 0]
_____



[Notes]

If no arguments are given, return [0, 0, 0, 0, 0, 0]


[arrays] [conditions] [loops] 



-------------------------------------------------------------------
[Resources]
_________
*args and **kwargs in Python
https://www.geeksforgeeks.org/args-kwargs-python/
The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-le …
_________
_________
Python For Loops
https://www.w3schools.com/python/python_for_loops.asp
Used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
_________
_________
type() Method
https://www.geeksforgeeks.org/python-type-function/
Returns class type of the argument(object) passed as parameter. type() function is mostly used for debugging purposes. Two different types of arguments can be passed to …
_________
_________
OrderedDict
https://www.geeksforgeeks.org/ordereddict-in-python/
Preserves the order in which the keys are inserted. A regular dict doesn’t track the insertion order, and iterating it gives the values in an arbitrary order. By contra …
_________

"""
#Your code should go here:

