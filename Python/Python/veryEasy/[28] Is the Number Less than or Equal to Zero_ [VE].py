"""
##Is the Number Less than or Equal to Zero?

Create a function that takes a number as its only argument and returns True if it's less than or equal to zero, otherwise return False.


[Examples]

___
less_than_or_equal_to_zero(5) ➞ False

less_than_or_equal_to_zero(0) ➞ True

less_than_or_equal_to_zero(-2) ➞ True
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[conditions] [language_fundamentals] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Less Than or Equal To ( <= )
https://python-reference.readthedocs.io/en/latest/docs/operators/less_eq.html
Returns a Boolean stating whether one expression is less than or equal the other.
_________
_________
Python Decision Making
https://www.tutorialspoint.com/python/python_decision_making.htm
Decision making is anticipation of conditions occurring while execution of the program and specifying actions taken according to the conditions.
_________
_________
Python Basic Operators
https://www.tutorialspoint.com/python/python_basic_operators.htm
Operators are the constructs which can manipulate the value of operands. Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.
_________
_________
Python Comparison Operators Example
https://www.tutorialspoint.com/python/comparison_operators_example.htm
These operators compare the values on either sides of them and decide the relation among them. They are also called Relational operators.
_________
_________
Conditional Statements
https://en.wikibooks.org/wiki/Python_Programming/Conditional_Statements
A Decision is when a program has more than one choice of actions depending on a variable's value. Think of a traffic light. When it is green, we continue our drive. Whe …
_________
_________
Conditionals
https://www.openbookproject.net/thinkcs/python/english2e/ch04.html
The modulus operator works on integers (and integer expressions) and yields the remainder when the first operand is divided by the second. In Python, the modulus operat …
_________
_________
Comparison Operators
https://data-flair.training/blogs/python-comparison-operators/#:~:text=Less%20Than%20or%20Equal%20To%20(%3C%3D)%20Operator&text=We%20will%20quickly%20learn%20how,the%20right%20of%20the%20operator.
Learn Python less than,Python greater than,equal to,not equal to less than,greater than or equal to Operators syntax.
_________
""" 
# Your code should go here:

def zerOrLess(num1):
    if num1 <= 0:
        return True
    else:
        return False

print(zerOrLess(5))
print(zerOrLess(0))
print(zerOrLess(-5))
print(zerOrLess(100))

# The program is complete.