"""
##Frequency Distribution

Create a function that returns the frequency distribution of a list. This function should return an object, where the keys are the unique elements and the values are the frequency in which those elements occur.


[Examples]

___
get_frequencies(["A", "B", "A", "A", "A"]) ➞ { "A" : 4, "B" : 1 }

get_frequencies([1, 2, 3, 3, 2]) ➞ { 1: 1, 2: 2, 3: 2 }

get_frequencies([True, False, True, False, False]) ➞ { True: 2, False: 3 }

get_frequencies([]) ➞ {}
_____



[Notes]

___
*) If given an empty list, return an empty object (see example #4).
*) The object should be in the same order as in the input list.
___



[language_fundamentals] [loops] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Finding frequency distribution of a list of numbers in Python?
https://stackoverflow.com/questions/40553332/finding-frequency-distribution-of-a-list-of-numbers-in-python
I have a Long list of numbers like the following. I would like to find frequency distribution of each number, but I could not use Counter function to get frequency of e …
_________
_________
Counter from Collections Module
https://pymotw.com/2/collections/counter.html
A Counter is a container that keeps track of how many times equivalent values are added. It can be used to implement the same algorithms for which bag or multiset data …
_________
_________
count() Method
https://www.programiz.com/python-programming/methods/list/count
Returns the number of times the specified element appears in the list.
_________
_________
Python Dictionary Comprehension
https://stackoverflow.com/questions/14507591/python-dictionary-comprehension
Is it possible to create a dictionary comprehension in Python (for the keys)? Without list comprehensions, you can use something like this: l = [] for n in range(1, 1 …
_________
_________
The Pythonic Way to Count Objects
https://realpython.com/python-counter/
In this step-by-step tutorial, you'll learn how to use Python's Counter to count several repeated objects at once.
_________
_________
setdefault() Method
https://www.tutorialspoint.com/python/dictionary_setdefault.htm
Similar to get(), but will set dict[key]=default if key is not already in dict.
_________
_________
get() Method
https://www.tutorialspoint.com/python/dictionary_get.htm
Returns a value for the given key. If key is not available then returns default value None.
_________
""" 
# Your code should go here:

