"""
##Less Than 100?

Given two numbers, return True if the sum of both numbers is less than 100. Otherwise return False.


[Examples]

___
less_than_100(22, 15) ➞ True
# 22 + 15 = 37

less_than_100(83, 34) ➞ False
# 83 + 34 = 117

less_than_100(3, 77) ➞ True
_____



[Notes]

N/A


[language_fundamentals] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to Do Math in Python with Operators
https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators
Numbers are extremely common in programming. They are used to represent things like screen size dimensions, geographic locations, money and points, the amount of time t …
_________
_________
Python Conditions
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics: Equals: a == b Not Equals: a != b Less than: a < b Less than or equal to: a <= b Greater than: a > b Grea …
_________
_________
Basic Operators
https://www.tutorialspoint.com/python/python_basic_operators.htm
Operators are the constructs which can manipulate the value of operands. Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.
_________
_________
bool() Function
https://www.w3schools.com/python/ref_func_bool.asp
Returns the boolean value of a specified object.
_________
_________
Video Walk Through the Challenge
https://youtube.com/watch?v=4z6K3hyHs2U
A video walkthrough of this challenge.
_________
""" 
# Your code should go here:

def lessThan100(num1, num2):
    if (num1 + num2) < 100:
        return True
    else:
        return False

print(lessThan100(100, 0))
print(lessThan100(99, 0))
print(lessThan100(32, 45))
print(lessThan100(43, 64))
print(lessThan100(0 , 0))

# The program is complete.