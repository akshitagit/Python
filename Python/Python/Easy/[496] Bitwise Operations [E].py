"""
##Bitwise Operations

A decimal number can be represented as a sequence of bits. To illustrate:
___
6 = 00000110
23 = 00010111
_____

From the bitwise representation of numbers, we can calculate the bitwise AND, bitwise OR and bitwise XOR. Using the example above:
___
bitwise_and(6, 23) ➞ 00000110

bitwise_or(6, 23) ➞ 00010111

bitwise_xor(6, 23) ➞ 00010001
_____

Write three functions to calculate the bitwise AND, bitwise OR and bitwise XOR of two numbers.


[Examples]

___
bitwise_and(7, 12) ➞ 4

bitwise_or(7, 12) ➞ 15

bitwise_xor(7, 12) ➞ 11
_____



[Notes]

N/A


[bit_operations] [language_fundamentals] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Python Bitwise Operators Example
https://www.tutorialspoint.com/python/bitwise_operators_example.htm
List of bitwise operators for the Python language.
_________
_________
Python Bitwise Operators with Syntax and Examples
https://data-flair.training/blogs/python-bitwise-operators/
In this tutorial, we discuss Python Bitwise AND, OR, XOR, Left-shift, Right-shift, and 1’s complement Bitwise Operators in Python Programming. Along with this, we will …
_________
_________
Python BitWise Operators
https://www.youtube.com/watch?v=PyfKCvHALj8
Lets work more on Operators. In this video we will see: - Bitwise Operators - Example of Bitwise Operators - Complement Operator - Tilde sign - Negative number, 2's Com …
_________
_________
Converting integer to binary in Python?
https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python
In order to convert an integer to a binary, i have used this code : >>> bin(6) '0b110' and when to erase the '0b', i use this : >>> bin(6)[2:] '110' What can i do if i …
_________
_________
What do the operators "<<, >>, &, |, ~, and ^" do?
https://wiki.python.org/moin/BitwiseOperators
All of these operators share something in common -- they are "bitwise" operators. That is, they operate on numbers (normally), but instead of treating that number as if …
_________
_________
Bitwise Operation
https://en.wikipedia.org/wiki/Bitwise_operation
In digital computer programming, a bitwise operation operates on one or more bit patterns or binary numerals at the level of their individual bits. It is a fast and sim …
_________
""" 
# Your code should go here:

