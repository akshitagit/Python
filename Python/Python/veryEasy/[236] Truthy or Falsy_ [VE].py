"""
##Truthy or Falsy?

A "truthy" value is a value that translates to True when evaluated in a Boolean context. All values are truthy unless they're defined as falsy.
All falsy values are as follows:
___
*) False
*) None
*) 0
*) []
*) {}
*) ""
___

Create a function that takes an argument of any data type and returns 1 if it's truthy and 0 if it's falsy.


[Examples]

___
is_truthy(0) ➞ 0

is_truthy(False) ➞ 0

is_truthy("") ➞ 0

is_truthy("False") ➞ 1
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[conditions] [control_flow] [language_fundamentals] [validation] 



-------------------------------------------------------------------
[Resources]
_________
bool() in Python
https://www.geeksforgeeks.org/bool-in-python/
Used to return or convert a value to a Boolean value i.e. True or False, using the standard truth testing procedure.
_________
_________
What is Truthy and Falsy? How is it different from True and False?
https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false
I just came to know there are Truthy and Falsy values in python which are different from the normal True and False? Can someone please explain in depth what truthy and …
_________
_________
True==1 and False==0
https://stackoverflow.com/questions/2764017/is-false-0-and-true-1-an-implementation-detail-or-is-it-guaranteed-by-the
Is it guaranteed that False == 0 and True == 1, in Python (assuming that they are not reassigned by the user)?
_________
_________
Use of Falsy and Truthy Concepts in Python
https://www.thetaranights.com/idiomatic-python-use-of-falsy-and-truthy-concepts/
Out of many, one reason for python’s popularity is the readability. Python has code style guidelines and idioms and these allow future readers of the code to comprehend …
_________
_________
Booleans
https://www.w3schools.com/python/python_booleans.asp
In fact, there are not many values that evaluates to False, except empty values, such as (), [], {},  "", the number 0, and the value None.  And of course the valu …
_________
_________
Truthy and Falsy Values in Python: A Detailed Introduction
https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/
Expressions with operands and operators evaluate to either True or False and they can be used in an if or while condition to determine if a code block should run.
_________
""" 
# Your code should go here:

