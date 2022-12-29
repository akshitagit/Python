"""
####  Sum of List Elements Except Itself  ####

A list is given. Return a new list having the sum of all its elements except itself. For more clarity, check the examples below.


[Clarification]

___
*) [1, 2, 3, 4] = for first element => sum will be 2+3+4 = [9]
*) [1, 2, 3, 4] = for second element => sum will be 1+3+4 = [9, 8]
*) [1, 2, 3, 4] = for third element => sum will be 1+2+4 = [9, 8, 7]
*) [1, 2, 3, 4] = for fourth element => sum will be 1+2+3 = [9, 8, 7, 6]
___



[Examples]

___
lst_ele_sum([1, 2, 3, 2, 1]) ➞ [8, 7, 6, 7, 8]

lst_ele_sum([1, 2]) ➞ [2, 1]

lst_ele_sum([1, 2, 3]) ➞ [5, 4, 3]

lst_ele_sum([1, 2, 3, 4, 5]) ➞ [14, 13, 12, 11, 10]

lst_ele_sum([10, 20, 30, 40, 50, 60]) ➞ [200, 190, 180, 170, 160, 150]
_____



[Notes]

N/A


[arrays] 



-------------------------------------------------------------------
[Resources]
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
A Complete Guide on List Slicing and slice() Method of Python
https://www.pickupbrain.com/python/complete-guide-list-slicing/
Slicing is extraction of a part of a sequence like list, tuple, string. It can fetch multiple elements at once with a single statement. It does not remove the values fr …
_________
_________
List Comprehension
https://www.w3schools.com/python/python_lists_comprehension.asp
Offers a shorter syntax when you want to create a new list based on the values of an existing list.
_________

"""
#Your code should go here:

