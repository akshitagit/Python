"""
##Minimal I: If Boolean Then Boolean

In this series we're going to see common redundancies and superfluities that make our code unnecessarily complicated and less readable, and we're going to learn how to avoid them.
In line with the spirit of the series, we can summarize the general rules of minimalist code in two simple principles:
___
*) Keep your code clean and readable.
*) While not violating the first principle: get rid of everything superfluous.
___

In order to achieve this you should:
___
*) Deepen your knowledge of logics.
*) Deepen your understanding of the particular language you're coding with.
___

I would also add: observe and learn from the pros. Make a habit of checking the Solutions tab after solving a challenge on Edabit.
There is absolutely nothing wrong in assimilating features of someone else's coding style, especially if yours is not yet fully developed.


[Goal]

In the Code tab you will find a code that is missing a single character in order to pass the tests. However, YOUR GOAL is to submit a function as minimalist as possible. Use the tips in the Tips section down below.
Write a function that returns True if the given integer is even, and False if it's odd.


[Tips]

Using an if statement in order to return boolean or to set a variable to a boolean is redundant.
A function that returns True if a person's age is 18 or greater and False otherwise, could be written as:
___
def legal_age(age):
  if age >= 18:
    return True
  else:
    return False
_____

Notice that age >= 18 will already give us a boolean (True or False). This means that the function can be written in a much simpler and cleaner way:
___
def legal_age(age):
  return age >= 18
_____



[Notes]

___
*) This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your suggestions in the Comment tab.
*) Readability is indeed a subjective concept. Let's discuss it! Feel free to leave your opinion in the Comments tab.
*) You can find all the exercises in this series over here.
___



[conditions] [language_fundamentals] [logic] [validation] 



-------------------------------------------------------------------
[Resources]
_________
What Does the % Symbol Mean in Python?
https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/
The % symbol in Python is called the Modulo Operator. It returns the remainder of dividing the left hand operand by right hand operand. It's used to get the remainder o …
_________
_________
Python Conditions
https://www.w3schools.com/python/python_conditions.asp
In this example we use two variables, a and b,
 which are used as part of the if statement to test whether b is greater than a.
 As a is 33, and b is 200,
 we know that …
_________
_________
Python Booleans
https://www.w3schools.com/python/python_booleans.asp
In programming you often need to know if an expression is True or False. You can evaluate any expression in Python, and get one of two answers, True or False. When yo …
_________
_________
not Keyword
https://www.w3schools.com/python/ref_keyword_not.asp
Is a logical operator. The return value will be True if the statement(s) are not True, otherwise it will return False.
_________
""" 
# Your code should go here:

def trueFalseInt(int1):
    return True if int1 % 2 == 0 else False

print(trueFalseInt(5))
print(trueFalseInt(6))
print(trueFalseInt(0))
print(trueFalseInt(99))

# The program is complete.
