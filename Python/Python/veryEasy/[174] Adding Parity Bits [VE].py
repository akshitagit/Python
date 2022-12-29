"""
##Adding Parity Bits

Parity bits are used as very simple checksum to ensure that binary data isn't corrupted during transit. Here's how they work:
___
*) If a binary string has an odd number of 1s, the parity bit is a 1.
*) If a binary string has an even number of 1s, the parity bit is a 0.
*) The parity bit is appended to the end of the binary string.
___

Create a function that adds the correct parity bit to a binary string.


[Worked Example]

___
add_parity_bit("1011011") ➞ "10110111"

# There are five 1s.
# Since five is odd, the parity bit should be a 1.
# Add the parity bit to the end of the string.
# Return the result.
_____



[Examples]

___
add_parity_bit("0010110") ➞ "00101101"

add_parity_bit("1100000") ➞ "11000000"

add_parity_bit("1111111") ➞ "11111111"
_____



[Notes]

All inputs will be 7-bits long (so that the parity bit makes it a full byte).


[logic] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String count() Method
https://www.tutorialspoint.com/python/string_count.htm
Returns the number of occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
_________
_________
count() Method
https://www.w3schools.com/python/ref_list_count.asp
Returns the number of elements with the specified value.
_________
""" 
# Your code should go here:

