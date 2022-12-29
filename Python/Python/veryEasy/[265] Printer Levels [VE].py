"""
##Printer Levels

Given a dictionary of how many more pages each ink color can print, output the maximum number of pages the printer can print before any of the colors run out.


[Examples]

___
ink_levels({
  "cyan": 23,
  "magenta": 12,
  "yellow": 10
}) ➞ 10

ink_levels({
  "cyan": 432,
  "magenta": 543,
  "yellow": 777
}) ➞ 432

ink_levels({
  "cyan": 700,
  "magenta": 700,
  "yellow": 0
}) ➞ 0
_____



[Notes]

A single printed page requires each color once, so printing is not possible if any of the slots lack ink (see example #3).


[arrays] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
values( ) Method
https://www.programiz.com/python-programming/methods/dictionary/values
Returns a view object that displays a list of all the values in the dictionary.
_________
_________
min() Method
https://www.programiz.com/python-programming/methods/built-in/min
Returns the smallest item in an iterable. It can also be used to find the smallest item between two or more parameters.
_________
_________
How to Sort a Dictionary by Values in Python
https://thomas-cokelaer.info/blog/2017/12/how-to-sort-a-dictionary-by-values-in-python/
By definition, dictionary are not sorted (to speed up access). Let us consider the following dictionary, which stores the age of several persons as values. If you want …
_________
_________
What does this mean: key=lambda x: x[1] ?
https://stackoverflow.com/questions/16310015/what-does-this-mean-key-lambda-x-x1
I see it used in sorting, but what do the individual components of this line of code actually mean? key=lambda x: x[1] What's lambda, what is x:, why [1] in x[1] etc ...
_________
""" 
# Your code should go here:

