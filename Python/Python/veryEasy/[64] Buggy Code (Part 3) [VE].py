"""
##Buggy Code (Part 3)

Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to get an idea of what the function should do.


[Examples]

___
sum_lst([1, 2, 3, 4, 5]) ➞ 15

sum_lst([-1, 0, 1]) ➞ 0

sum_lst([0, 4, 8, 12]) ➞ 24
_____



[Notes]

___
*) READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!
*) Don't overthink this challenge; it's not supposed to be hard.
___



[arrays] [bugs] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Sum of All the Elements in a List
https://www.programminginpython.com/python-program-calculate-sum-elements-list/
A simple python program which calculates the sum of all the elements in a list. Here we use a predefined function sum() on the list to calculate its sum.
_________
_________
For Loops
https://www.w3schools.com/python/python_for_loops.asp
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other program …
_________
_________
len() Function
https://www.w3schools.com/python/ref_func_len.asp
Returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.
_________
_________
sum() Function
https://www.geeksforgeeks.org/sum-function-python/
Sum of numbers in the list is required everywhere. Python provides an inbuilt function sum() which sums up the numbers in the list.
_________
""" 
# Your code should go here:

def sumListLoop(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum
def sumListMethod(list1):
    return sum(list1)

print(sumListLoop([1, 2, 3, 4, 5]))
print(sumListMethod([1, 2, 3, 4, 5]))

print(sumListLoop([-1, 0, 1]))
print(sumListMethod([-1, 0, 1]))

print(sumListLoop([0, 4, 8, 12]))
print(sumListMethod([0, 4, 8, 12]))

# The program is complete.