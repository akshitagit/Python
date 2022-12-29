"""
##Largest Swap

Write a function that takes a two-digit number and determines if it's the largest of two possible digit swaps.
To illustrate:
___
largest_swap(27) ➞ False

largest_swap(43) ➞ True
_____

If 27 is our input, we should return False because swapping the digits gives us 72, and 72 > 27. On the other hand, swapping 43 gives us 34, and 43 > 34.


[Examples]

___
largest_swap(14) ➞ False

largest_swap(53) ➞ True

largest_swap(99) ➞ True
_____



[Notes]

Numbers with two identical digits (third example) should yield True (you can't do better).


[logic] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to turn a single number into single digits?
https://stackoverflow.com/questions/21270320/turn-a-single-number-into-single-digits-python
Shows how to split a large integer into bite size chunks so that large integers can be individualized, subsequently sorted, and have notation or conditions applied.
_________
_________
Splitting integer in Python?
https://stackoverflow.com/questions/1906717/splitting-integer-in-python
My integer input is suppose 12345, I want to split and put it into an array as 1, 2, 3, 4, 5. How will I be able to do it?
_________
_________
How to reverse a String in Python
https://www.w3schools.com/python/python_howto_reverse_string.asp
In this particular example, the slice statement [::-1] means start at  the end of the string and end at position 0, move with the  step -1, negative one, which means …
_________
_________
What's the difference between "/" and "//" when used for division?
https://stackoverflow.com/questions/183853/what-is-the-difference-between-and-when-used-for-division
Is there a benefit to using one over the other? They both seem to return the same results.
_________
_________
How to find the division remainder of a number in Python?
https://stackoverflow.com/questions/5584586/find-the-division-remainder-of-a-number
How could I go about finding the division remainder of a number in Python? For example: If the number is 26 and divided number is 7, then the division remainder is 5 ( …
_________
""" 
# Your code should go here:

