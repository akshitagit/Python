"""
####  Majority Vote  ####

Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).


[Examples]

___
majority_vote(["A", "A", "B"]) ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
_____



[Notes]

___
*) The frequency of the majority element must be strictly greater than 1/2.
*) If there is no majority element, return None.
*) If the list is empty, return None.
___



[arrays] [loops] 



-------------------------------------------------------------------
[Resources]
_________
count() Method
https://www.programiz.com/python-programming/methods/list/count
Returns the number of occurrences of an element in a list.
_________
_________
Understanding the set() Method in Python
https://stackoverflow.com/questions/15181867/understanding-the-set-function
In python, set() is an unordered collection with no duplicate elements. However, I am not able to understand how it generates the output. For example, consider the foll …
_________
_________
Majority Element
https://www.geeksforgeeks.org/majority-element/
The basic solution is to have two loops and keep track of maximum count for all different elements. If maximum count becomes greater than n/2 then break the loops and r …
_________

"""
#Your code should go here:

