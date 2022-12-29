"""
####  Last Digit Ultimate  ####

Your job is to create a function, that takes 3 numbers: a, b, c and returns True if the last digit of a * b = the last digit of c. Check the examples below for an explanation.


[Examples]

___
last_dig(25, 21, 125) ➞ True
# The last digit of 25 is 5, the last digit of 21 is 1, and the last
# digit of 125 is 5, and the last digit of 5*1 = 5, which is equal
# to the last digit of 125(5).

last_dig(55, 226, 5190) ➞ True
# The last digit of 55 is 5, the last digit of 226 is 6, and the last
# digit of 5190 is 0, and the last digit of 5*6 = 30 is 0, which is
# equal to the last digit of 5190(0).

last_dig(12, 215, 2142) ➞ False
# The last digit of 12 is 2, the last digit of 215 is 5, and the last
# digit of 2142 is 2, and the last digit of 2*5 = 10 is 0, which is
# not equal to the last digit of 2142(2).
_____



[Notes]

Numbers can be negative.


[algebra] [logic] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Find First and Last Digits of a Number
https://www.geeksforgeeks.org/find-first-last-digits-number/
To find last digit of a number, we use modulo operator %. When modulo divided by 10 returns its last digit. Suppose if n = 1234 then last Digit = n % 10 => 4 To finding …
_________
_________
% modulus
https://python-reference.readthedocs.io/en/latest/docs/operators/modulus.html
Returns the decimal part (remainder) of the quotient.
_________

"""
#Your code should go here:

