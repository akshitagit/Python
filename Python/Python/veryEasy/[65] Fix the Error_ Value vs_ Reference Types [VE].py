"""
##Fix the Error: Value vs. Reference Types

Create a function that returns True if two lists contain identical values, and False otherwise.
To solve this question, your friend writes the following code:
___
def check_equals(lst1, lst2):
    if lst1 is lst2:
        return True
    else:
        return False
_____

But testing the code, you see that something is not quite right. Running the code yields the following results:
___
check_equals([1, 2], [1, 3]) ➞ False
# Good so far...

check_equals([1, 2], [1, 2]) ➞ False
# Yikes! What happened?
_____

Rewrite your friend's code so that it correctly checks if two lists are equal. To be equal, the lists must have the same elements in the same order. The tests below should pass:


[Examples]

___
check_equals([1, 2], [1, 3]) ➞ False

check_equals([1, 2], [1, 2]) ➞ True

check_equals([4, 5, 6], [4, 5, 6]) ➞ True

check_equals([4, 7, 6], [4, 5, 6]) ➞ False
_____



[Notes]

Hint: This has to do with value vs. reference types.


[bugs] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to Compare Two Lists
https://www.stechies.com/compare-lists-python-using-set-cmp-function/
This tutorial explains how to compare Lists in Python using Set() and Cmp() Function. two very common methods of comparison are set() and cmp(). In this tutorial you wi …
_________
_________
How to check if two lists are identical?
https://www.geeksforgeeks.org/python-check-if-two-lists-are-identical/
This article deals with the task of ways to check if two unordered list contains exact similar elements in exact similar position, i.e to check if two lists are exactly …
_________
""" 
# Your code should go here:

def chkIdenticality(list1, list2):
    if list1 == list2:
        return True
    else:
        return False

print(chkIdenticality([1, 2], [1, 3]))
print(chkIdenticality([1, 2], [1, 2]))
print(chkIdenticality([4, 5, 6], [4, 5, 6]))
print(chkIdenticality([4, 7, 6], [4, 5, 6]))

# The program is complete.