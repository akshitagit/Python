"""
####  Subset Validation  ####

Write a function that returns True if all subsets in a list belong to a given set.


[Examples]

___
validate_subsets([[1, 2], [2, 3], [1, 3]], [1, 2, 3]) ➞ True

validate_subsets([[1, 2, 3], [2], [3], []], [1, 2, 3]) ➞ True

validate_subsets([[1, 2], [2, 3], [1, 4]], [1, 2, 3]) ➞ False

validate_subsets([[1, 2, 3, 4]], [1, 2, 3]) ➞ False
_____



[Notes]

___
*) The empty set and the set itself are both valid subsets of a set (we are not talking about proper subsets here).
*) The set and the subset will each have unique elements.
___



[higher_order_functions] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Any & All in Python
https://www.tutorialspoint.com/any-and-all-in-python
The any() function returns True if any item in an iterable are true, otherwise it returns False. However, if the iterable object is empty, the any () function will retu …
_________
_________
issubset() Method
https://www.w3schools.com/python/ref_set_issubset.asp
Returns True if all items in the set exists in the specified set, otherwise it retuns False.
_________
_________
Nested If Statements with List Comprehension
https://stackoverflow.com/questions/42488400/python-nested-if-statements-with-list-comprehension
How can you nest multiple ifs while you have list comprehension? As you can see example function takes optional parameters. So if a or b is passed to func1 only x that …
_________

"""
#Your code should go here:

