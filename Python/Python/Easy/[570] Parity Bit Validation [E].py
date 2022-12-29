"""
##Parity Bit Validation

Parity bits are used as very simple checksum to ensure that binary data isn't corrupted during transit. Here's how they work:
___
*) If a binary string has an odd number of 1s, the parity bit is a 1.
*) If a binary string has an even number of 1s, the parity bit is a 0.
*) The parity bit is appended to the end of the binary string.
___

Create a function that validates whether a binary string is valid, using parity bits.


[Worked Example]

___
validate_binary("10110010") ➞ True

# The last digit is the parity bit.
# 0 is the last digit.
# 0 means that there should be an even number of 1s.
# There are four 1s.
# Return True.
_____



[Examples]

___
validate_binary("00101101") ➞ True

validate_binary("11000000") ➞ True

validate_binary("11000001") ➞ False
_____



[Notes]

___
*) All inputs will be a byte long (8 characters).
*) You can find another parity bit involved challenge here!
___



[numbers] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to Use Python Lambda Functions
https://realpython.com/python-lambda/
In this step-by-step tutorial, you'll learn about Python lambda functions. You'll see how they compare with regular functions and how you can use them in accordance wit …
_________
_________
count() Method
https://www.w3schools.com/python/ref_list_count.asp
Return the number of times the value '1' appears in the binary list of 1's and 0's.
_________
""" 
# Your code should go here:

