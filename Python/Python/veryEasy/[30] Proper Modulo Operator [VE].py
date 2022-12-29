"""
##Proper Modulo Operator

Create a function which returns the Modulo of the two given numbers.


[Examples]

___
mod(-13, 64) ➞ 51

mod(50, 25) ➞ 0

mod(-6, 3) ➞ 0
_____



[Notes]

All test cases contain valid numbers.


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Modulo Operator
https://www.geeksforgeeks.org/what-is-a-modulo-operator-in-python/
When we see a ‘%’ the first thing that comes to our mind is the “Percentage-sign”, but when we think of it from the perspective of computer language, this sign has, in …
_________
_________
Python Modulo operator
https://www.jquery-az.com/python-modulo/#:~:text=In%20Python%20and%20generally%20speaking%2C%20the%20modulo%20%28or,numbers%20are%20first%20converted%20in%20the%20common%20type.
In Python and generally speaking, the modulo (or modulus) is referred to as the remainder from the division of the first argument to the second. The symbol used to get …
_________
""" 
# Your code should go here:

def mod(num1, num2):
    return (num1 % num2)

print(mod(-13, 64))
print(mod(50, 25))
print(mod(-6, 3))
print(mod(33, 11))
print(mod(11,2))

# The program is complete.