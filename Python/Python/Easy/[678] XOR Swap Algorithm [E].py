"""
####  XOR Swap Algorithm  ####

This is more informational than a challenge. You can actually switch 2 variables with the XOR operation ^. XOR works with two arguments. It turns both arguments into their binary representations, and for each bit, returns 1 if they are different, 0 otherwise.
The return value is the decimal representation of the new binary string. So, if you don't know how to do it, go play around with it! After some time on paper, you will understand what is going on, and how it works.
Your job is to switch 2 variables using the XOR operator, which means your return statement should be return[a, b], but the values stored in the variables need to be switched.


[Examples]

___
XOR(10, 41) ➞ (41, 10)

XOR(69, 420) ➞ (420, 69)

XOR(12345, 890412) ➞ (890412, 12345)
_____



[For this challenge, avoid doing the following:]

___
def XOR(a, b):
  return[b, a]
_____

___
def XOR(a, b):
  temp = a
  a = b
  b = temp
  return[a, b]
_____



[Notes]

If you're stuck, or don't have time to test out different cases, check the Resources tab.


[bit_operations] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Swap Two Variables Using XOR
https://betterexplained.com/articles/swap-two-variables-using-xor/
It almost seems like magic, the same statement is repeated 3 times and voila, the values magically swap? Let’s take a closer look.
_________
_________
How to Swap Variables
https://www.geeksforgeeks.org/python-program-to-swap-two-variables/#:~:text=The%20bitwise%20XOR%20operator%20can,0101)%20is%20(0010).
Given two variables x and y, write a Python program to swap their values. Let’s see different methods in Python to do this task.
_________
_________
XOR Swap Algorithm
https://en.wikipedia.org/wiki/XOR_swap_algorithm
Is an algorithm that uses the XOR bitwise operation to swap values of distinct variables having the same data type without using a temporary variable. "Distinct" means …
_________

"""
#Your code should go here:

