"""
####  Add the Values of the Symbols in a Matrix  ####

Write a function that takes a list of lists and returns the value of all of the symbols in it, where each symbol adds or takes something from the total score. Symbol values:
___
*) # = 5
*) O = 3
*) X = 1
*) ! = -1
*) !! = -3
*) !!! = -5
___

A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.
If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.


[Examples]

___
check_score([
  ["#", "!"],
  ["!!", "X"]
]) ➞ 2

check_score([
  ["!!!", "O", "!"],
  ["X", "#", "!!!"],
  ["!!", "X", "O"]
]) ➞ 0

check_score([
  ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
  ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
  ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
  ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
  ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
  ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
  ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
  ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
  ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
  ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
  ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
  ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
  ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
  ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
]) ➞ 12
_____



[Notes]

Strings in the lists will only be #, O, X, !, !! and !!!.


[functional_programming] [math] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
max() Function
https://www.programiz.com/python-programming/methods/built-in/max
Returns the largest item in an iterable. It can also be used to find the largest item between two or more parameters.
_________
_________
Ternary Operator
https://www.geeksforgeeks.org/ternary-operator-in-python/
Also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. It simply a …
_________
_________
Dictionaries
https://realpython.com/python-dicts/
In this Python dictionaries tutorial you'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, yo …
_________
_________
For Loops
https://www.w3schools.com/python/python_for_loops.asp
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
_________
_________
How to Flatten a List of Lists
https://note.nkmk.me/en/python-list-flatten/
To flatten a list of lists (a multi-dimensional list, nested list) in Python, you can use itertools.chain.from_iterable(), sum(), etc.Flatten 2D list (a list of lists)i …
_________

"""
#Your code should go here:

