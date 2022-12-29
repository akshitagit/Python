"""
##Increment to Top

Create a function that returns the total number of steps it takes to transform each element to the maximal element in the list. Each step consists of incrementing a digit by one.


[Examples]

___
increment_to_top([3, 4, 5]) ➞ 3
# Maximal element in the array is 5.
# To transform 3 to 5 requires 2 steps: 3 -> 4, 4 -> 5.
# To transform 4 to 5 requires 1 step: 4 -> 5.
# Total steps required is 3.

increment_to_top([4, 3, 4]) ➞ 1
# Maximal element in the array is 4.
# To transform 3 to 4 requires 1 steps: 3 -> 4.
# Total steps required is 1.

increment_to_top([3, 3, 3]) ➞ 0

increment_to_top([3, 10, 3]) ➞ 14
_____



[Notes]

___
*) If the list contains only the same digits, return 0 (see example #3).
*) Bonus: Can you write a solution that achieves this by only traversing the list once? (i.e. without finding the max beforehand)
___



[arrays] [logic] [loops] 



-------------------------------------------------------------------
[Resources]
_________
max() Method
https://www.programiz.com/python-programming/methods/built-in/max
Returns the smallest item in an iterable. It can also be used to find the smallest item between two or more parameters.
_________
_________
Comprehensions in Python
https://www.geeksforgeeks.org/comprehensions-in-python/
Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been alread …
_________
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
Return largest integer in the list?
https://stackoverflow.com/questions/17916293/python-return-largest-integer-in-the-list
I am new to python and am trying to work with lists. how can i get my function to accept a list of integers and then returns the largest integer in the list?
_________
""" 
# Your code should go here:

