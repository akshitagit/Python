"""
##CMS Selector Based on a Given String

Write a function that takes a list of strings and a pattern (string) and returns the strings that contain the pattern in alphabetical order. If the pattern is an empty string, return all the strings passed in the input list.


[Examples]

___
cms_selector(["WordPress", "Joomla", "Drupal"], "w") ➞ ["WordPress"]

cms_selector(["WordPress", "Joomla", "Drupal", "Magento"], "ru") ➞ ["Drupal"]

cms_selector(["WordPress", "Joomla", "Drupal", "Magento"], "") ➞ ["Drupal", "Joomla", "Magento", "WordPress"]
_____



[Notes]

___
*) The given letter(s) are case insensitive and can be more than one.
*) In the case of an empty string, return the entire list.
*) A CMS is a Content Management System.
___



[arrays] [formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to find a substring within a list?
https://stackoverflow.com/questions/13779526/finding-a-substring-within-a-list-in-python
Example list: mylist = ['abc123', 'def456', 'ghi789'] I want to retrieve an element if there's a match for a substring, like abc Code: sub = 'abc' print any(sub in my …
_________
_________
sorted() Method
https://www.w3schools.com/python/ref_func_sorted.asp
Returns a sorted list of the specified iterable object. You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numeric …
_________
""" 
# Your code should go here:

