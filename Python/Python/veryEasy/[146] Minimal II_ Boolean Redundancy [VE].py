"""
##Minimal II: Boolean Redundancy

Check the principles of minimalist code in the intro to the first challenge.
In the Code tab you will find a code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section down below.
Write a function that returns the string "even" if the given integer is even, and the string "odd" if it's odd.


[Tips]

Converting a boolean, or something that will ultimately be interpreted as a boolean, into a boolean is redundant.
For example, the code:
___
boolean = bool(x < 4)
return boolean == True
_____

Is equivalent to simply:
___
return x < 4
_____

___
*) A comparison with <, <=, ==, !=, >=, > will always result in a boolean, therefore using the function bool() is totally unnecessary.
*) boolean == True is redundant, as it will always return boolean.
*) To obtain the opposite of boolean we could use boolean == False. However, a much cleaner way of doing this is simply not boolean.
*) While preserving readability, avoid declaring unnecessary variables.
___



[Notes]

___
*) This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your suggestions in Comments.
*) Readability is indeed a subjective concept. Let's discuss it! Feel free to leave your opinion in Comments.
*) You can find all the exercises in this series over here.
___



[conditions] [language_fundamentals] [logic] 



-------------------------------------------------------------------
[Resources]
_________
What Does the % Symbol Mean in Python?
https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/
The % symbol in Python is called the Modulo Operator. It returns the remainder of dividing the left hand operand by right hand operand. It's used to get the remainder o …
_________
_________
Ternary Operator
https://www.geeksforgeeks.org/ternary-operator-in-python/
Are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. It simply allows to test a condition in a single …
_________
_________
Python Booleans
https://www.w3schools.com/python/python_booleans.asp
In programming you often need to know if an expression is True or False. You can evaluate any expression in Python, and get one of two answers, True or False. When yo …
_________
_________
Python Conditions
https://www.w3schools.com/python/python_conditions.asp
In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that …
_________
""" 
# Your code should go here:

