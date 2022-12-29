"""
##ReverseAndNot

Write a function that takes an integer i and returns an integer with the integer backwards followed by the original integer.
To illustrate:
___
123
_____

We reverse 123 to get 321 and then add 123 to the end, resulting in 321123.


[Examples]

___
reverse_and_not(123) ➞ 321123

reverse_and_not(152) ➞ 251152

reverse_and_not(123456789) ➞ 987654321123456789
_____



[Notes]

i is a non-negative integer.


[formatting] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
join() Method
https://www.geeksforgeeks.org/join-function-python/
A string method and returns a string in which the elements of sequence have been joined by str separator
_________
_________
reversed() Method
https://www.programiz.com/python-programming/methods/built-in/reversed
Returns the reversed iterator of the given sequence
_________
_________
How to Reverse a String
https://www.w3schools.com/python/python_howto_reverse_string.asp
There is no built-in function to reverse a String in Python. The fastest (and easiest?) way is to use a slice that steps backwards, -1.
_________
_________
str() Method
https://www.w3schools.com/python/ref_func_str.asp
Converts the specified value into a string.
_________
""" 
# Your code should go here:

