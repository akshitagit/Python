"""
##Curzon Numbers

In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.


[Examples]

___
is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11

is_curzon(10) ➞ False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21

is_curzon(14) ➞ True
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29
_____



[Notes]

N/A


[math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Curzon Numbers
http://www.numbersaplenty.com/set/Curzon_number/more.php
A number n such that 2n + 1 divides 2n + 1.
_________
_________
The Python Modulo Operator
https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/
The % symbol in Python is called the Modulo Operator. It returns the remainder of dividing the left hand operand by right hand operand. It's used to get the remainder o …
_________
_________
what is difference between (**) and (<<)?
https://stackoverflow.com/questions/19882922/what-is-difference-between-and-in-python
** is the exponent operator. << shifts bits to the left. Because of the nature of binary numbers, for every step shifting bits to the left doubles the number.
_________
_________
Curzon Numbers
https://www.geeksforgeeks.org/curzon-numbers/#:~:text=Given%20an%20integer%20N%2C%20check,by%202*N%20%2B%201.
Given an integer N, check whether the given number is a Curzon Number or not.
_________
""" 
# Your code should go here:

def isCurzon(num1):
    if (((2**num1)+1)%((2*num1)+1)) == 0:
        return True
    else:
        return False

print(isCurzon(5))
print(isCurzon(10))
print(isCurzon(14))
print(isCurzon(50))
print(isCurzon(53))
print(isCurzon(65))
print(isCurzon(13))

# The program is complete.