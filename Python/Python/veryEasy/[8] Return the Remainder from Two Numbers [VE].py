"""
##Return the Remainder from Two Numbers

There is a single operator in Python, capable of providing the remainder of a division operation. Two numbers are passed as parameters. The first parameter divided by the second parameter will have a remainder, possibly zero. Return that value.


[Examples]

___
remainder(1, 3) ➞ 1

remainder(3, 4) ➞ 3

remainder(5, 5) ➞ 0

remainder(7, 2) ➞ 1
_____



[Notes]

___
*) The tests only use positive integers.
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
___



[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Python Basic Operators
https://www.tutorialspoint.com/python/python_basic_operators.htm
Operators are the constructs which can manipulate the value of operands. Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.
_________
_________
Remainder
https://en.wikipedia.org/wiki/Remainder
The remainder is the amount "left over" after performing some computation. In arithmetic, the remainder is the integer "left over" after dividing one integer by another …
_________
_________
What is the result of % in Python?
https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python
What does the % in a calculation? I can't seem to work out what it does. Does it work out a percent of the calculation for example: 4 % 2 is apparently equal to 0. How?
_________
_________
Python Modulo in Practice: How to Use the % Operator
https://realpython.com/python-modulo-operator/
In this tutorial, you'll learn about the Python modulo operator (%). You'll look at the mathematical concepts behind the modulo operation and how the modulo operator is …
_________
""" 
# Your code should go here:

def remainder(num1, num2):
    if num1 > 0 and num2 > 0:
        return (num1 % num2)
    else:
        return ("Please input positive numericals.")

print(remainder(1,3))
print(remainder(3,4))
print(remainder(5,5))
print(remainder(7,2))
print(remainder(10,0))

# The program is complete.