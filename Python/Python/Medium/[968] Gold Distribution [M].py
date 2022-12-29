"""
####  Gold Distribution  ####

A group of pirates each have a distribution of gold coins, which can be represented as a list:
___
[3, 9, 4, 5, 5]
# Pirate 1 has 3 gold, Pirate 2 has 9 gold, etc.
_____

The difference between each pirate's share of gold and that of the richest pirate is represented as:
___
[6, 0, 5, 4, 4]
# Since 6 = 9 - 3, 0 = 9 - 9, 4 = 9 - 5, etc.
_____

Pirates have a keen sense of fairness, and a pirate will kill the others if he deems his share to be too little. Each pirate has a unique inequality threshold - the maximum difference he is willing to tolerate before he kills his comrades.
Using the above gold distribution:
___
[5, 0, 5, 5, 5]
# Pirates killed, since 5 < 6.
# 5 is Pirate 1's inequality distribution and 6 is his gold difference.

[7, 0, 5, 5, 5]
# Pirate 1 is satisfied, since 7 > 6.
# All other pirates are satisfied as well.
_____

Given a distribution of coins and a list of inequality thresholds, create a function that returns True if any pirates are killed, or False otherwise.


[Examples]

___
pirates_killed([3, 5, 8, 3, 4], [10, 4, 2, 5, 5]) ➞ False

pirates_killed([3, 5, 8, 3, 4], [10, 4, 2, 5, 1]) ➞ True

pirates_killed([3, 3, 10], [7, 7, 0]) ➞ False

pirates_killed([3, 3, 10], [6, 6, 0]) ➞ True
_____



[Notes]

___
*) A pirate kills if the difference in his share of gold from the richest pirate is strictly greater than his inequality threshold.
*) Gold and inequality distribution lists are both ordered the same. (e.g. Pirate 1 is index 0 for both lists, Pirate 2 is index 1 for both lists, etc).
___



[arrays] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
any() Method
https://www.programiz.com/python-programming/methods/built-in/any
Returns True if any element of an iterable is True. If not, any() returns False.
_________
_________
zip() Method
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and return it. In this tutorial, we will learn about Python zip() in detail with the help of examples.
_________
_________
max() Function
https://www.programiz.com/python-programming/methods/built-in/max
Returns the largest item in an iterable. It can also be used to find the largest item between two or more parameters.
_________

"""
#Your code should go here:

