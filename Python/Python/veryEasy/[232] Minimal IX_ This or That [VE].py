"""
##Minimal IX: This or That

Check the principles of minimalist code in the intro to the first challenge.
In the Code tab you will find a code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section below.
Write a function that returns the first truthy argument passed to the function. If all arguments are falsy, return the string "not found". The function will be called with a minimum of one and a maximum of four arguments: a, b, c, d.


[Tips]

The operator or can be used to assign or return the first truthy value among two or more elements. If no truthy value is found, the last element will be returned.
For example, the code:
___
def one_of_these(a, b, c):
    return a if a else b if b else c
_____

Can be simplified to:
___
def one_of_these(a, b, c):
    return a or b or c
_____



[Bonus]

Once a truthy value is found, the rest of the elements will not be checked. This can be used to define a sort of default value that will be returned if all of the previous elements happen to be false or empty:
___
txt1 = ""
txt2 = "Edabit"

txt1 or "Empty string" ➞ "Empty string"
txt2 or "Empty string" ➞ "Edabit"
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
Ternary Operator
https://www.geeksforgeeks.org/ternary-operator-in-python/
Are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. It simply allows to test a condition in a single …
_________
_________
Operators
https://www.w3schools.com/python/python_operators.asp
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
_________
_________
*args and **kwargs
https://www.programiz.com/python-programming/args-and-kwargs
In this article, we will learn about Python *args and **kwargs ,their uses and functions with examples.
_________
""" 
# Your code should go here:

