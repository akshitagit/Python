"""
####  Peeling off the Outer Layers  ####

Given a list of lists, return a new list of lists containing every element, except for the outer elements.


[Examples]

___
peel_layer_off([
  ["a", "b", "c", "d"],
  ["e", "f", "g", "h"],
  ["i", "j", "k", "l"],
  ["m", "n", "o", "p"]
]) ➞ [
  ["f", "g"],
  ["j", "k"]
]

peel_layer_off([
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25],
  [26, 27, 28, 29, 30],
  [31, 32, 33, 34, 35]
]) ➞ [
  [7, 8, 9],
  [12, 13, 14],
  [17, 18, 19],
  [22, 23, 24],
  [27, 28, 29]
]

peel_layer_off([
  [True, False, True],
  [False, False, True],
  [True, True, True]
]) ➞ [[False]]

peel_layer_off([
  ["hello", "world"],
  ["hello", "world"]
]) ➞ []
_____



[Notes]

___
*) The 2D grid is always a rectangular/square shape.
*) Always return some form of nested list, unless there are no elements. In that case, return an empty list.
___



[arrays] [language_fundamentals] [loops] 



-------------------------------------------------------------------
[Resources]
_________
List Comprehensions
https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in …
_________
_________
pop() Function
https://www.geeksforgeeks.org/python-list-pop/#:~:text=pop()%20is%20an%20inbuilt,is%20popped%20out%20and%20removed.
Is an inbuilt function in Python that removes and returns last value from the list or the given index value.
_________
_________
Indexing and Slicing
https://www.stat.berkeley.edu/~spector/extension/python/notes/node19.html
Strings in python support indexing and slicing. To extract a single character from a string, follow the string with the index of the desired character surrounded by squ …
_________
_________
Slicing a Multi-Dimensional Array
https://stackoverflow.com/questions/17277100/python-slicing-a-multi-dimensional-array
I'm new to Python and numpy. I've figured out how to slice 1 dimensional sequence: arr[start:end], and access an element in the array: el = arr[row][col]. Trying somet …
_________
_________
Convert NumPy Array to List
https://www.journaldev.com/32797/python-convert-numpy-array-to-list
We can use numpy ndarray tolist() function to convert the array to a list. If the array is multi-dimensional, a nested list is returned. For one-dimensional array, a li …
_________

"""
#Your code should go here:

