"""
####  Minimal III: You're a Boolean Now  ####

Check the principles of minimalist code in the intro to the first challenge.
In the Code tab you will find code that is missing a single character in order to pass the tests. However, your goal is to submit a function that is as minimalist as possible. Use the tips in the tips section below.
Write a function that returns True if the given positive integer is a prime number and False if it's not.


[Tips]

Everything you write after if, not, while or around and, or, is, in is interpreted as a boolean.
A function that prints a countdown from the absolute value of x and also prints "hey" if the number is a multiple of 3 and contains the digit "3", could be written as:
___
def countdown(x):
    if x < 0:
        x = x * -1
    while x > 0:
        if x % 3 == 0:
            if "3" in str(x):
                print(x)
                print("hey")
        else:
            print(x)
        x = x - 1
_____

This can be simplified to:
___
def countdown(x):
    x = abs(x)
    while x:
        print(x)
        if not x % 3 and "3" in str(x):
            print("hey")
        x -= 1
_____

___
*) abs() gets the absolute value of a number.
*) while will interpret x as a boolean, exiting the loop after reaching zero.
*) print(x) needs to be called whether x is a "hey number" or not. This can be done outside of any if statement, instead of in both.
*) Both conditions x % 3 == 0 and "3" in str(x) need to be True, so they can be joined with an and.
___



[Bonus]

A more Pythonistic approach:
___
def countdown(x):
    for i in range(abs(x), -1, -1):
        print(x)
        if not x % 3 and "3" in str(x):
            print("hey")
_____



[Notes]

___
*) This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your suggestions in the Comment tab.
*) Readability is indeed a subjective concept. Let's discuss it! Feel free to leave your opinion in the Comments tab.
*) You can find all the exercises in this series over here.
___



[conditions] [language_fundamentals] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Python Conditions
https://www.w3schools.com/python/python_conditions.asp
In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that …
_________
_________
Prime Number
https://en.wikipedia.org/wiki/Prime_number
A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime i …
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
_________

"""
#Your code should go here:

