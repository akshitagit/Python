"""
##Check if One List is a Subset of Another

List A is contained inside list B if each element in A also exists in B.
The number of times a number is present doesn't matter. In other words, if we transformed both lists into sets, A would be a subset of B.
___
A = [3, 3, 9, 9, 9, 5]
B = [1, 3, 9, 5, 8, 44, 44]

A_Set = [3, 9, 5]
B_Set = [1, 3, 9, 5, 8, 44]

# A_Set is a subset of B_Set
_____

Create a function that determines if the first list is a subset of the second.


[Examples]

___
subset([1, 3], [1, 3, 3, 5]) ➞ True

subset([4, 8, 7], [7, 4, 4, 4, 9, 8]) ➞ True

subset([1, 3], [1, 33]) ➞ False

subset([1, 3, 10], [10, 8, 8, 8]) ➞ False
_____



[Notes]

___
*) Each input list will have at least one element.
*) Check the resources tab for a hint.
___



[arrays] [logic] [validation] 



-------------------------------------------------------------------
[Resources]
_________
issubset() Method
https://www.w3schools.com/python/ref_set_issubset.asp
Returns True if all items in the set exists in the specified set, otherwise it returns False.
_________
_________
Set Types — set, frozenset
https://docs.python.org/3.7/library/stdtypes.html#set-types-set-frozenset
A set object is an unordered collection of distinct hashable objects. Common uses include membership testing, removing duplicates from a sequence, and computing mathema …
_________
_________
issubset() Method
https://www.programiz.com/python-programming/methods/set/issubset
Returns True if all elements of a set are present in another set (passed as an argument). If not, it returns False.
_________
_________
How to check if all of the following items are in a list?
https://stackoverflow.com/questions/3931541/how-to-check-if-all-of-the-following-items-are-in-a-list
I found, that there is related question, about how to find if at least one item exists in a list: How to check if one of the following items is in a list? But what is t …
_________
""" 
# Your code should go here:

