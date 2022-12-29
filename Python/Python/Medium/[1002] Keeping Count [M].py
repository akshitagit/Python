"""
####  Keeping Count  ####

Given a number, create a function that returns a new number based on these rules:
___
*) For each digit, replace it by the number of times it appears in the number.
*) The final instance of the number will be an integer, not a string.
___



[Worked Example]

___
digit_count(136116) ➞ 312332
# The number 1 appears thrice, so replace all 1s with 3s.
# The number 3 appears only once, so replace all 3s with 1s.
# The number 6 appears twice, so replace all 6s with 2s.
# Return as an integer.
_____



[Examples]

___
digit_count(221333) ➞ 221333

digit_count(136116) ➞ 312332

digit_count(2) ➞ 1
_____



[Notes]

All test input will be positive whole numbers.


[language_fundamentals] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
str() Function
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object. In this tutorial, we will learn about Python str() in detail with the help of examples.
_________
_________
String join() Method
https://www.tutorialspoint.com/python/string_join.htm
Returns a string in which the string elements of sequence have been joined by str separator.
_________
_________
String count() Method
https://www.programiz.com/python-programming/methods/string/count
Returns the number of occurrences of a substring in the given string.
_________
_________
List Comprehension
https://www.learnbyexample.org/python-list-comprehension/
Learn List Comprehension in Python with syntax and lots of examples, list comprehension with if else, nested list comprehension and much more.
_________
_________
Count Occurrences of an Element in a List
https://www.geeksforgeeks.org/python-count-occurrences-element-list/
Given a list in Python and a number x, count number of occurrences of x in the given list.
_________

"""
#Your code should go here:

