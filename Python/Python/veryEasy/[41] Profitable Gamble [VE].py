"""
##Profitable Gamble

Create a function that takes three arguments prob, prize, pay and returns True if prob * prize > pay; otherwise return False.
To illustrate:
___
profitable_gamble(0.2, 50, 9)
_____

... should yield True, since the net profit is 1 (0.2 * 50 - 9), and 1 > 0.


[Examples]

___
profitable_gamble(0.2, 50, 9) ➞ True

profitable_gamble(0.9, 1, 2) ➞ False

profitable_gamble(0.9, 3, 2) ➞ True
_____



[Notes]

A profitable gamble is a game that yields a positive net profit, where net profit is calculated in the following manner: net_outcome = probability_of_winning * prize - cost_of_playing.


[conditions] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
One line if statement in Python (ternary conditional operator) 
https://www.pythoncentral.io/one-line-if-statement-in-python-ternary-conditional-operator/
We look at how you can use one line if statements in Python, otherwise known as the ternary operator. How it is used, and what alternatives are available.
_________
_________
What does return True/False actually do?
https://stackoverflow.com/questions/28513250/what-does-return-true-false-actually-do-python
I always see programs with if statements that return True or False, but what is actually happening here, why wouldn't you just want to put a print statement for false/true?
_________
_________
Python Operators: Arithmetic, Comparison, Logical and more
https://www.programiz.com/python-programming/operators
In this article, you'll learn everything about different types of operators in Python, their syntax and how to use them with examples.
_________
""" 
# Your code should go here:

def gambProf(prob, prize, pay):
    if ((prob * prize) > pay):
        return True
    else:
        return False

print(gambProf(0.2, 50, 9))
print(gambProf(0.9, 1, 2))
print(gambProf(0.9, 3, 2))

# The program is complete.