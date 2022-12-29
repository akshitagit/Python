"""
##Remove Duplicates from a List

Create a function that takes a list of items, removes all duplicate items and returns a new list in the same sequential order as the old list (minus duplicates).


[Examples]

___
remove_dups([1, 0, 1, 0]) ➞ [1, 0]

remove_dups(["The", "big", "cat"]) ➞ ["The", "big", "cat"]

remove_dups(["John", "Taylor", "John"]) ➞ ["John", "Taylor"]
_____



[Notes]

___
*) Tests contain lists with both strings and numbers.
*) Tests are case sensitive.
*) Each list item is unique.
___



[arrays] [interview] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Converting a list to a set changes element order?
https://stackoverflow.com/questions/9792664/set-changes-element-order
Recently I noticed that when I am converting a list to set the order of elements is changed and is sorted by character. Consider this example: x = [1, 2, 20, 6, 210] …
_________
_________
Python Lists
https://developers.google.com/edu/python/lists
Python has a great built-in list type named "list". List literals are written within square brackets [ ]. Lists work similarly to strings -- use the len() function and …
_________
_________
How to Remove Duplicates from a List While Preserving Order in Python
http://www.martinbroadhurst.com/removing-duplicates-from-a-list-while-preserving-order-in-python.html
You can remove duplicates from a list easily by putting the elements in a set and then making a new list from the set’s contents. However, this will put the elements in …
_________
_________
Quick Trick to Remove Duplicates in a List
https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists#7961390
The common approach to get a unique collection of items is to use a set. Sets are unordered collections of distinct objects. To create a set from any iterable, you can …
_________
_________
Iterate Over a Set in Python
https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
There are numerous ways that can be used to iterate over a Set. Some of these ways provide faster time execution as compared to others. Some of these ways include, iter …
_________
_________
Removing duplicates in Python lists?
https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
Pretty much I need to write a program to check if a list has any duplicates and if it does it removes them and returns a new list with the items that werent duplicated/ …
_________
""" 
# Your code should go here:

