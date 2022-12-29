"""
####  Neutralisation  ####

Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:
___
*) When positives and positives interact, they remain positive.
*) When negatives and negatives interact, they remain negative.
*) But when negatives and positives interact, they become neutral, and are shown as the number 0.
___



[Worked Example]

___
neutralise("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.
_____



[Examples]

___
neutralise("--++--", "++--++") ➞ "000000"

neutralise("-+-+-+", "-+-+-+") ➞ "-+-+-+"

neutralise("-++-", "-+-+") ➞ "-+00"
_____



[Notes]

The two strings will be the same length.


[conditions] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
Use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables in parallel and create dictionaries with just a few …
_________
_________
join() Method
https://www.w3schools.com/python/ref_string_join.asp
Takes all items in an iterable and joins them into one string. A string must be specified as the separator.
_________
_________
range() Function
https://www.w3schools.com/python/ref_func_range.asp
Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
_________
_________
Ternary Operator
https://data-flair.training/blogs/python-ternary-operator/
Are terse conditional expressions. These are operators that test a condition and based on that, evaluate a value. This was made available since PEP 308 was approved and …
_________
_________
Enumerate() Method
https://www.geeksforgeeks.org/enumerate-in-python/
Adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of …
_________
_________
pop() Method
https://www.w3schools.com/python/ref_list_pop.asp
Removes the element at the specified position.
_________

"""
#Your code should go here:

