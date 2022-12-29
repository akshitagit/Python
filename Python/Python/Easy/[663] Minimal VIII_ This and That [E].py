"""
####  Minimal VIII: This and That  ####

Check the principles of minimalist code in the intro to the first challenge.
In the Code tab you will find a code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section below.
Write a function that returns the third character of the third string in a given list of strings. Return False if it can't be found.


[Tips]

The operator and can be used to assign or return the first falsy value among two or more elements. If no falsy value is found, the last element will be returned.
For example, the code:
___
def all_of_these(a, b, c):
    return a if not a else b if not b else c
_____

Can be simplified to:
___
def all_of_these(a, b, c):
    return a and b and c
_____



[Bonus]

Once a falsy value is found, the rest of the elements will not be checked. For example, if we wanted to access the first element of a list, but the list happened to be empty, we would get an error. We can use and to work around this issue:
___
lst1 = [1, 2, 3]
lst2 = []

lst1 and lst1[0] ➞ 1
lst2 and lst2[0] ➞ []
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
Idiomatic Python: EAFP versus LBYL
https://devblogs.microsoft.com/python/idiomatic-python-eafp-versus-lbyl/
One idiomatic practice in Python that often surprises people coming from programming languages where exceptions are considered, well, exceptional, is EAFP: “it’s easier …
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
_________
_________
Try Except
https://www.w3schools.com/python/python_try_except.asp
The try block lets you test a block of code for errors. The except block lets you handle the error. The finally block lets you execute code, regardless of the result …
_________

"""
#Your code should go here:

