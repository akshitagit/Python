"""
##Return the First Element in a List

Create a function that takes a list containing only numbers and return the first element.


[Examples]

___
get_first_value([1, 2, 3]) ➞ 1

get_first_value([80, 5, 100]) ➞ 80

get_first_value([-500, 0, 50]) ➞ -500
_____



[Notes]

The first element in a list always has an index of 0.


[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
How to access list elements?
https://stackoverflow.com/questions/10613131/how-to-access-list-elements
I have a list: list = [['vegas','London'],['US','UK']] How to access each element of this list?
_________
_________
Python Lists (with examples)
https://www.programiz.com/python-programming/list
In this article, we'll learn everything about Python lists; how they are created, slicing of a list, adding or removing elements from them and so on.
_________
_________
IndexError: list index out of range
https://www.codecademy.com/forum_questions/50b9043a205619d28a0001a2
I was playing around with this exercise, trying to get the same output a different way. Why do I get this error? Is it because 'i' starts at 1 and the list starts at 0?
_________
_________
How to Access List Elements
https://www.w3schools.com/python/gloss_python_access_list_items.asp
You access the list items by referring to the index number...
_________
_________
Get First and Last Elements of a List
https://www.geeksforgeeks.org/python-get-first-and-last-elements-of-a-list/
Sometimes, there might be a need to get the range between which a number lies in the list, for such applications we require to get the first and last element of the lis …
_________
_________
Lists
https://www.geeksforgeeks.org/python-list/
Are just like dynamic sized arrays, declared in other languages (vector in C++ and ArrayList in Java). Lists need not be homogeneous always which makes it a most powerf …
_________
_________
Lists
https://www.w3schools.com/python/python_lists.asp
Are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
_________
_________
Video Walk Through the Challenge
https://youtu.be/FfGTh_qm-WU
A video walkthrough of this challenge.
_________
""" 
# Your code should go here:

def firstElement(list1):
    return list1[0]

print(firstElement([1, 2, 3]))
print(firstElement([80, 5, 100]))
print(firstElement([-500,0,50]))

# The program is complete.