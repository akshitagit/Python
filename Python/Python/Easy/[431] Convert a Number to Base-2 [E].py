"""
##Convert a Number to Base-2

Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.
Going from right to left, the value of the most right bit is 1, now from that every bit to the left will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).


[Examples]

___
binary(1) ➞ "1"
# 1*1 = 1

binary(5) ➞ "101"
# 1*1 + 1*4 = 5

binary(10) ➞ "1010"
# 1*2 + 1*8 = 10
_____



[Notes]

___
*) Numbers will always be below 1024 (not including 1024).
*) The strings will always go to the length at which the most left bit's value gets bigger than the number in decimal.
*) If a binary conversion for 0 is attempted, return "0".
___



[bit_operations] [logic] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How to convert decimal to binary in Python?
https://stackoverflow.com/questions/3528146/convert-decimal-to-binary-in-python
Is there any module or function in python I can use to convert a decimal number to its binary equivalent? I am able to convert binary to decimal using int('[binary_valu …
_________
_________
Decimal to Binary Converter
https://www.rapidtables.com/convert/number/decimal-to-binary.html
Decimal to binary number converter and how to convert.
_________
_________
bin() Method
https://www.programiz.com/python-programming/methods/built-in/bin
Converts and returns the binary equivalent string of a given integer. If the parameter isn't an integer, it has to implement __index__() method to return an integer.
_________
_________
Writing Binary Numbers
https://wild.maths.org/writing-binary-numbers
Before writing numbers in binary, let's remind ourselves of how we usually write numbers using decimal notation. Let's take the number 4302 as an example. The digit 4 i …
_________
""" 
# Your code should go here:

