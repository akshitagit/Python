"""
##Coding Website Score Calculator

Imagine you run a website that presents users with different coding challenges in levels Easy, Medium, and Hard, where users get points for completing challenges. An Easy challenge is worth 5 points, a Medium challenge is worth 10 points, and a Hard challenge is worth 20 points.
Create a function that takes the amount of challenges a user has completed for each challenge level, and calculates the user's total number of points. Keep in mind that a user cannot complete negative challenges, so the function should return the string "invalid" if any of the passed parameters are negative.


[Examples]

___
score_calculator(1, 2, 3) ➞ 85

score_calculator(1, 0, 10) ➞ 205

score_calculator(5, 2, -6) ➞ "invalid"
_____



[Notes]

N/A


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Identify a Negative Number in a List
https://stackoverflow.com/questions/15993583/python-identify-a-negative-number-in-a-list/15993606
This article describes how to identify the negative numbers in a list. It also tells how to find the number of the negative numbers in the list.
_________
_________
map( ) Function with lambda Expressions
https://www.programiz.com/python-programming/methods/built-in/map
Applies a function to all elements of an iterable. Lambda (anonymous) functions can be used to determine the condition. Returns True or False in that case. Usefull to d …
_________
_________
all( ) Method
https://www.programiz.com/python-programming/methods/built-in/all
Similar to the SQL operator. It is a universal quantifier that acts on an iterable. True if all elements of the iterable are different from 0 or False. You can use list …
_________
_________
If Statement
https://pythonexamples.org/python-if-example/
Learn about Python If statement syntax and different scenarios where Python If statement can be used.
_________
""" 
# Your code should go here:

