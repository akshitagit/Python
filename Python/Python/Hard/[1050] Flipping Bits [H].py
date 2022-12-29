"""
####  Flipping Bits  ####

You will be given a list of 32-bit unsigned integers. Flip all the bits 1 -> 0 and 0 -> 1 and return the result as an unsigned integer.


[Worked Example]

___
n = 4
4 is 0100 in binary. We are working in 32 bits so:
00000000000000000000000000000100 = 4
11111111111111111111111111111011 = 4294967291
return 4294967291
_____



[Examples]

___
flipping_bits(2147483647) ➞ 2147483648

flipping_bits(1) ➞ 4294967294

flipping_bits(4) ➞ 4294967291
_____



[Notes]

N/A


[bit_operations] [formatting] 



-------------------------------------------------------------------
[Resources]
_________
bin() Method
https://www.programiz.com/python-programming/methods/built-in/bin
Converts and returns the binary equivalent string of a given integer. If the parameter isn't an integer, it has to implement __index__() method to return an integer.
_________
_________
Bitwise Operators
https://realpython.com/python-bitwise-operators/
Learn how to use Python's bitwise operators to manipulate individual bits of data at the most granular level. With the help of hands-on examples, you'll see how you can …
_________
_________
zfill() Method
https://www.w3schools.com/python/ref_string_zfill.asp
Adds zeros (0) at the beginning of the string, until it reaches the specified length.
_________
_________
Converting Binary to Decimal Integer Output
https://stackoverflow.com/questions/21765779/converting-binary-to-decimal-integer-output
I need to convert a binary input into a decimal integer. I know how to go from a decimal to a binary. I need to go in the reverse direction. My professor said that when …
_________

"""
#Your code should go here:

