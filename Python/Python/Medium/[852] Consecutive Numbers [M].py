"""
####  Consecutive Numbers  ####

Create a function that determines whether elements in an array can be re-arranged to form a consecutive list of numbers where each number appears exactly once.


[Examples]

___
cons([5, 1, 4, 3, 2]) ➞ True
// Can be re-arranged to form [1, 2, 3, 4, 5]

cons([5, 1, 4, 3, 2, 8]) ➞ False

cons([5, 6, 7, 8, 9, 9]) ➞ False
// 9 appears twice
_____



[Notes]

N/A


[arrays] [loops] [sorting] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to see if the list contains consecutive numbers?
https://stackoverflow.com/questions/33575235/how-to-see-if-the-list-contains-consecutive-numbers
For the whole list, it should just be as simple as sorted(l) == list(range(min(l), max(l)+1)) This preserves the original list, but making a copy (and then sorting) may …
_________
_________
Sorting HOW TO
https://docs.python.org/3/howto/sorting.html
Python lists have a built-in list.sort() method that modifies the list in-place. There is also a sorted() built-in function that builds a new sorted list from an iterable.
_________
_________
max() and min()
https://www.geeksforgeeks.org/max-min-python/
max() is used to compute the maximum of the values passed in its argument and lexicographically largest value if strings are passed as arguments. min() is used to compu …
_________
_________
range() Method
https://www.w3schools.com/python/ref_func_range.asp
Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
_________

"""
#Your code should go here:

