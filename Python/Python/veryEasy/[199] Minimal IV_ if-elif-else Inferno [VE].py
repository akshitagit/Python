"""
##Minimal IV: if-elif-else Inferno

Check the principles of minimalist code in the intro to the first challenge.
In the Code tab you will find a code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section below.
Write a function that returns the boolean True if the given number is zero, the string "positive" if the number is greater than zero or the string "negative" if it's smaller than zero.


[Tips]

Executing a return will effectively end your function.
For example, the code:
___
def compare_to_100(x):
    if x > 100:
        return "greater"
    elif x < 100:
        return "smaller"
    else:
        return "equal"
_____

Can be simplified to:
___
def compare_to_100(x):
    if x > 100:
        return "greater"
    if x < 100:
        return "smaller"
    return "equal"
_____

___
*) If x is greater than 100, Python will not execute the code past the first return.
*) If x is smaller than 100, Python will not execute the code inside the first if statement or past the second return.
*) If x is equal to 100, Python will not execute the code inside the two if statements.
*) This can only be used if you have a return inside your if statement.
___



[Bonus]

Further simplification of the code above:
___
def compare_to_100(x):
    return "greater" if x > 100 else "smaller" if x < 100 else "equal"
_____



[Notes]

___
*) This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your suggestions in the Comments.
*) Readability is indeed a subjective concept. Let's discuss it! Feel free to leave your opinion in the Comments.
*) You can find all the exercises in this series over here.
___



[conditions] [language_fundamentals] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Ternary Operator in Python
https://www.geeksforgeeks.org/ternary-operator-in-python/
Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in versio …
_________
_________
Python IF, ELSE, ELIF, Nested IF & Switch Case Statement
https://www.guru99.com/if-loop-python-conditional-structures.html
In this tutorial, learn Conditional Statements in Python. Learn how to use If, Else, Elif, Nested IF and Switch Case Statements with examples.
_________
_________
Python Conditions
https://www.w3schools.com/python/python_conditions.asp
In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that …
_________
""" 
# Your code should go here:

