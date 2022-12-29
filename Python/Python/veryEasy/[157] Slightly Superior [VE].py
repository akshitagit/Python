"""
##Slightly Superior

You will be given two extremely similar lists, but exactly one of the items in a list will be valued slightly higher than its counterpart (which means that evaluating the value > the other value will return True).
Create a function that returns whether the first list is slightly superior to the second list.


[Examples]

___
is_first_superior([1, 2, 4], [1, 2, 3]) ➞ True
# The pair of items at each index are compared in turn.
# 1 from the first list is the same as 1 from the second list.
# 2 is the same as 2.
# However, 4 is greater than 3, so list one is superior.

is_first_superior(["a", "d", "c"], ["a", "b", "c"]) ➞ True

is_first_superior(["zebra", "ostrich", "whale"], ["ant", "ostrich", "whale"]) ➞ True

is_first_superior([1, 2, 3, 4], [1, 2, 4, 4]) ➞ False

is_first_superior([True, 10, "zebra"], [True, 10, "zebra"]) ➞ False
_____



[Notes]

___
*) Both lists will be the same length.
*) All values and their counterparts will always be the same data type.
*) The lists will only be different by one element.
*) If the two lists are the same, return False.
___



[language_fundamentals] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Comparing Two Lists Using the Greater Than or Less Than Operator
https://stackoverflow.com/a/47342743
The pair of items at each index are compared in turn. So, comparing a to b will result in 1 being compared to 1, 2 being compared to 2, and 3 being compared to 10. The …
_________
""" 
# Your code should go here:

