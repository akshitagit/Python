"""
##Convert Number to String of Dashes

Create a function that takes a number (from 1 - 60) and returns a corresponding string of hyphens.


[Examples]

___
num_to_dashes(1) ➞ "-"

num_to_dashes(5) ➞ "-----"

num_to_dashes(3) ➞ "---"
_____



[Notes]

___
*) You will be provided integers ranging from 1 to 60.
*) Don't forget to return your result as a string.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[loops] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to Use Python to Multiply Strings
https://www.pythoncentral.io/use-python-multiply-strings/
You can use Python to multiply strings, which is actually pretty cool when you think about it. You can take a string and double, triple, even quadruple it with only a l …
_________
_________
Itertools.chain()
https://www.geeksforgeeks.org/python-itertools-chain/
Is a module in Python having a collection of functions that are used for handling iterators. They make iterating through the iterables like lists and strings very easil …
_________
_________
How to Tame a Python
https://www.youtube.com/watch?v=a9tTGSGwpBQ
The fastest way to multiply string characters.
_________
_________
Python Strings
https://www.tutorialspoint.com/python/python_strings.htm
Strings are amongst the most popular types in Python. We can create them simply by enclosing characters in quotes. Python treats single quotes the same as double quotes …
_________
_________
Concatenation and Repetition
https://interactivepython.org/runestone/static/CS152f17/Lists/ConcatenationandRepetition.html
Again, as with strings, the + operator concatenates lists. Similarly, the * operator repeats the items in a list a given number of times.
_________
""" 
# Your code should go here:

numToDashes = lambda n : ("-" * n) if n >=1 and n <= 60 else "Please specify the proper range."

print("Actual outputs: ")
print(numToDashes(1))
print(numToDashes(5))
print(numToDashes(3))
print("\nConfirmation of tests:- ")
print("Type of outputs: ")
print(type(numToDashes(1)))
print(type(numToDashes(5)))
print(type(numToDashes(3)))

print("\nLengths of outputs:")
print(len(numToDashes(1)))
print(len(numToDashes(5)))
print(len(numToDashes(3)))

# The program is complete.