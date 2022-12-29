"""
##Check if an Integer is Divisible By Five

Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.


[Examples]

___
divisible_by_five(5) ➞ True

divisible_by_five(-55) ➞ True

divisible_by_five(37) ➞ False
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Basic Operators in Python
https://www.geeksforgeeks.org/basic-operators-python/
Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division. Relational Operators: Relational operators com …
_________
_________
Division Operators in Python
https://www.geeksforgeeks.org/division-operator-in-python/
First output is fine, but the second one may be surprising if we are coming Java/C++ world. In Python 2.7, the “/” operator works as a floor division for integer argume …
_________
_________
Basic Operators
https://www.tutorialspoint.com/python/python_basic_operators.htm
Operators are the constructs which can manipulate the value of operands. Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.
_________
_________
Python If... Else
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics. These conditions can be used in several ways, most commonly in "if statements" and loops. An "if statemen …
_________
_________
Operators: Arithmetic, Comparison, Logical and more.
https://www.programiz.com/python-programming/operators
In this tutorial, you'll learn everything about different types of operators in Python, their syntax and how to use them with examples.
_________
_________
Modulo Operator
https://www.geeksforgeeks.org/what-is-a-modulo-operator-in-python/
When we see a ‘%’ the first thing that comes to our mind is the “Percentage-sign”, but when we think of it from the perspective of computer language, this sign has, in …
_________
""" 
# Your code should go here:

def divby5(num1):
    if (num1 % 5) == 0:
        return True
    else:
        return False

print(divby5(5))
print(divby5(55))
print(divby5(37))
print(divby5(23))

# The program is complete.