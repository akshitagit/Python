"""
##Fix the Errors / Comparing Arrays

Programmer Pete is trying to create a function that returns True if two lists share the
same length and have identical numerical values at every index, otherwise, it will return False.
However, the solution his function gives is in an unexpected format.
Can you fix Pete's function so that it behaves as seen in the examples below?


[Examples]

___
check_equals([1, 2], [1, 3]) ➞ False

check_equals([1, 2], [1, 2]) ➞ True

check_equals([4, 5, 6], [4, 5, 6]) ➞ True

check_equals([4, 7, 6], [4, 5, 6]) ➞ False

check_equals([1, 12], [11, 2]) ➞ False
_____



[Notes]

Check the Resources tab for more info.


[arrays] [bugs] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Check If Two Lists Are Identical
https://www.geeksforgeeks.org/python-check-if-two-lists-are-identical/
This article deals with the task of ways to check if two unordered list contains exact similar elements in exact similar position, i.e to check if two lists are exactly …
_________
_________
Conditions
https://www.w3schools.com/python/python_conditions.asp
In this example we use two variables, a and b,
 which are used as part of the if statement to test whether b is greater than a.
 As a is 33, and b is 200,
 we know that …
_________
_________
List
https://www.learnbyexample.org/python-list/
Learn to create and access a list in Python, change add and remove list items, iterate a list, find list length, check if item exists in a list, list concatenation and …
_________
""" 
# Your code should go here:

def checkEquals(list1, list2):
    if len(list1) == len(list2):
        if list1 == list2:
            return True
        else:
            return False
    else:
        return "String's length do not match, each other."

print(checkEquals([1, 2], [1, 3]))
print(checkEquals([1, 2], [1, 2]))
print(checkEquals([4, 5, 6], [4, 5, 6]))
print(checkEquals([4, 7, 6], [4, 5, 6]))
print(checkEquals([1, 12], [11, 2]))
print(checkEquals([1, 2, 3], [1, 2]))

# The program is complete.