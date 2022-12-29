"""
####  Crowded Carriage Capacity  ####

A train has a maximum capacity of n passengers overall, which means each carriage's capacity will share an equal proportion of the maximum capacity.
Create a function which returns the index of the first carriage which holds 50% or less of its maximum capacity. If no such carriage exists, return -1.


[Worked Example]

___
find_a_seat(200, [35, 23, 18, 10, 40]) ➞ 2

# There are 5 carriages which each have a maximum capacity of 40 (200 / 5 = 40).
# Index 0's carriage is too full (35 is 87.5% of the maximum).
# Index 1's carriage is too full (23 is 57.5% of the maximum).
# Index 2's carriage is good enough (18 is 45% of the maximum).
# Return 2.
_____



[Examples]

___
find_a_seat(20, [3, 5, 4, 2]) ➞ 3

find_a_seat(1000, [50, 20, 80, 90, 100, 60, 30, 50, 80, 60]) ➞ 0

find_a_seat(200, [35, 23, 40, 21, 38]) ➞ -1
_____



[Notes]

___
*) This means if a train can hold 200 passengers, and has 5 carriages, then that means each carriage can hold a maximum of 40 passengers each.
*) All carriage numbers will be positive integers, which will be able to divide evenly.
*) Remember to return -1 if no carriage is empty enough.
___



[interview] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
List index() Method
https://www.w3schools.com/python/ref_list_index.asp
Returns the position at the first occurrence of the specified value.
_________
_________
len() Method
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
_________
enumerate() Method
https://www.geeksforgeeks.org/enumerate-in-python/
A lot of times when dealing with iterators, we also get a need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumer …
_________
_________
Try Except
https://www.w3schools.com/python/python_try_except.asp
The try block lets you test a block of code for errors. The except block lets you handle the error. The finally block lets you execute code, regardless of the result of …
_________

"""
#Your code should go here:

