"""
##Check if a List Contains a Given Number

Write a function to check if a list contains a particular number.


[Examples]

___
check([1, 2, 3, 4, 5], 3) ➞ True

check([1, 1, 2, 1, 1], 3) ➞ False

check([5, 5, 5, 6], 5) ➞ True

check([], 5) ➞ False
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[arrays] [language_fundamentals] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to check if an item exists in a list ?
https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/
In this article we will discuss different ways to check if a given element exists in list or not. Suppose we have a list of strings i.e. # List of string listOfStri …
_________
_________
What's the fastest way to check if a value exists in a list?
https://stackoverflow.com/questions/7571635/fastest-way-to-check-if-a-value-exists-in-a-list
What is the fastest way to know if a value exists in a list (a list with millions of values in it) and what its index is? I know that all values in the list are unique …
_________
_________
Video Walk Through the Challenge
https://youtube.com/watch?v=4z6K3hyHs2U
A video walkthrough of this challenge.
_________
_________
Does Python have a 'contains' function?
https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
Discusses what method is most alike to the contains function in other languages.
_________
_________
How to Check If an Item Exists in List?
https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/
In this article we will discuss different ways to check if a given element exists in list or not. Suppose we have a list of strings like so: listOfStrings = ['Hi' , 'he …
_________
_________
Python Lists
https://www.tutorialspoint.com/python/python_lists.htm
Make sure to read Python's documentation on lists, which include the Basic List Operation, including how to find an element within a list with the Operation 'in'
_________
""" 
# Your code should go here:

# def toCheck(list1, toCheck):
#     if toCheck in list1:
#         return True
#     else:
#         return False

toCheck = lambda list1, toCheck : True if toCheck in list1 else False

print(toCheck([1, 2, 3, 4, 5], 3))
print(toCheck([1, 1, 2, 1, 1], 3))
print(toCheck([5, 5, 5, 6], 5))
print(toCheck([], 5))

# The program is complete.