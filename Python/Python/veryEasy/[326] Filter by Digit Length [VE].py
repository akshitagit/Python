"""
##Filter by Digit Length

Create a function that filters out a list to include numbers that only have a certain number of digits.


[Examples]

___
filter_digit_length([88, 232, 4, 9721, 555], 3) ➞ [232, 555]
# Include only numbers with 3 digits.

filter_digit_length([2, 7, 8, 9, 1012], 1) ➞ [2, 7, 8, 9]
# Include only numbers with 1 digit.

filter_digit_length([32, 88, 74, 91, 300, 4050], 1) ➞ []
# No numbers with only 1 digit exist => return empty list.

filter_digit_length([5, 6, 8, 9], 1) ➞ [5, 6, 8, 9]
# All numbers in the list have 1 digit only => return original list.
_____



[Notes]

___
*) If no numbers of the specified digit length exist, return an empty list.
*) If all numbers in the list have the specified digit length, return the original list.
*) The sub-list returned should have the same relative order as the original list.
___



[arrays] [higher_order_functions] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How to count the number of digits in Python?
https://stackoverflow.com/questions/22656345/how-to-count-the-number-of-digits-in-python
I am trying to write a function that counts the number of digits in a given number. This is my function. But this function is not working. What should the condition be …
_________
_________
str() Method
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object. In this tutorial, we will learn about Python str() in detail with the help of examples.
_________
""" 
# Your code should go here:

