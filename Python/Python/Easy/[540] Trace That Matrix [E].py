"""
##Trace That Matrix

Given a square matrix (i.e. same number of rows as columns), its trace is the sum of the entries in the main diagonal (i.e. the diagonal line from the top left to the bottom right).
As an example, for:
___
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
_____

... the trace is 1 + 5 + 9 = 15.
Write a function that takes a square matrix and computes its trace.


[Examples]

___
trace([
  [1, 4],
  [4, 1]
]) ➞ 2

# 1 + 1 = 2

trace([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ 15

# 1 + 5 + 9 = 15

trace([
  [1, 0, 1, 0],
  [0, 2, 0, 2],
  [3, 0, 3, 0],
  [0, 4, 0, 4]
]) ➞ 10

# 1 + 2 + 3 + 4 = 10
_____



[Notes]

As in the examples, the size of the matrices will vary (but they will always be square).


[arrays] [language_fundamentals] [math] 



-------------------------------------------------------------------
[Resources]
_________
How to access am item in a list of lists?
https://stackoverflow.com/questions/18449360/access-item-in-a-list-of-lists
If I have a list of lists and just want to manipulate an individual item in that list, how would I go about doing that? For example: List1 = [[10, 13, 17], [3, 5, 1], [ …
_________
_________
matrix.trace() Method
https://www.geeksforgeeks.org/python-numpy-matrix-trace/
With the help of Numpy matrix.trace() method, we can find the sum of all the elements of diagonal of a matrix by using the matrix.trace() method.
_________
_________
Main Diagonal
https://chortle.ccsu.edu/VectorLessons/vmch13/vmch13_17.html
The main diagonal of a matrix consists of those elements that lie on the diagonal that runs from top left to bottom right.
_________
_________
Two-dimensional lists (arrays)
https://snakify.org/en/lessons/two_dimensional_lists_arrays/
In real-world Often tasks have to store rectangular data table. [say more on this!] Such tables are called matrices or two-dimensional arrays. In Python any table can b …
_________
""" 
# Your code should go here:

