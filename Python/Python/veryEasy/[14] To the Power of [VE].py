"""
##To the Power of _____

Create a function that takes a base number and an exponent number and returns the calculation.


[Examples]

___
calculate_exponent(5, 5) ➞ 3125

calculate_exponent(10, 10) ➞ 10000000000

calculate_exponent(3, 3) ➞ 27
_____



[Notes]

___
*) All test inputs will be positive integers.
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[logic] [loops] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
The Power Operator
https://docs.python.org/3/reference/expressions.html#the-power-operator
Binds more tightly than unary operators on its left; it binds less tightly than unary operators on its right.
_________
_________
Exponents
https://www.mathsisfun.com/exponent.html
The exponent of a number says how many times to use the number in a multiplication.
_________
_________
How To Do Math in Python with Operators
https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators
Numbers are extremely common in programming. They are used to represent things like screen size dimensions, geographic locations, money and points, the amount of time t …
_________
_________
Video Walk Through
https://www.youtube.com/watch?v=SKR-8fowFiE
In this video, you will learn how to solve these problems: 0:22 Return a String as an Integer, 1:31 Add, Subtract, Multiply or Divide?, 4:35 To the Power of ___...
_________
""" 
# Your code should go here:

def calcExpo(baseNum, expoNum):
    return (baseNum ** expoNum)

print(calcExpo(5,5))
print(calcExpo(10,10))
print(calcExpo(3,3))
print(calcExpo(2,2))

# The program is Complete.