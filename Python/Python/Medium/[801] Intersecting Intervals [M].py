"""
####  Intersecting Intervals  ####

Create a function that takes in a list of intervals and returns how many intervals overlap with a given point.
An interval overlaps a particular point if the point exists inside the interval, or on the interval's boundary. For example the point 3 overlaps with the interval [2, 4] (it is inside) and [2, 3] (it is on the boundary).
To illustrate:
___
count_overlapping([[1, 2], [2, 3], [1, 3], [4, 5], [0, 1]], 2) ➞ 3
# Since [1, 2], [2, 3] and [1, 3] all overlap with point 2
_____



[Examples]

___
count_overlapping([[1, 2], [2, 3], [3, 4]], 5) ➞ 0

count_overlapping([[1, 2], [5, 6], [5, 7]], 5) ➞ 2

count_overlapping([[1, 2], [5, 8], [6, 9]], 7) ➞ 2
_____



[Notes]

___
*) Each interval is represented as a list with a start point and an endpoint.
*) Intervals count as intersecting even if they only intersect at one point, i.e. [2, 3] and [3, 4] both intersect at point 3.
*) If it's helpful, you can draw these intervals on a line on a piece of paper.
___



[algorithms] [arrays] [validation] 



-------------------------------------------------------------------
[Resources]
_________
count() Method
https://www.programiz.com/python-programming/methods/list/count
Returns the number of times the specified element appears in the list.
_________
_________
List Comprehension
https://www.w3schools.com/python/python_lists_comprehension.asp
Offers a shorter syntax when you want to create a new list based on the values of an existing list.
_________
_________
How do I check whether an int is between the two numbers?
https://stackoverflow.com/questions/13628791/how-do-i-check-whether-an-int-is-between-the-two-numbers
I need to check whether a number is between two other numbers, 10000 and 30000: if number >= 10000 and number >= 30000: print ("you have to pay 5% taxes") It's not …
_________
_________
Python Ifs
https://www.guru99.com/if-loop-python-conditional-structures.html
Conditional Statement in Python perform different computations or actions depending on whether a specific Boolean constraint evaluates to true or false. Conditional sta …
_________

"""
#Your code should go here:

