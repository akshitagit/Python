"""
##Pair Management

Given two arguments, return a list which contains these two arguments.


[Examples]

___
make_pair(1, 2) ➞ [1, 2]

make_pair(51, 21) ➞ [51, 21]

make_pair(512124, 215) ➞ [512124, 215]
_____



[Notes]

N/A


[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Lists
https://www.geeksforgeeks.org/python-list/
Lists in Python can be created by just placing the sequence inside the square brackets[].
_________
_________
Return Multiple Values
https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/
In Python, we can return multiple values from a function. Following are 4 different ways to do so.
_________
_________
list() Function
https://www.w3schools.com/python/ref_func_list.asp
Creates a list object. A list object is a collection which is ordered and changeable.
_________
_________
Video Walking Through the Challenge
https://www.youtube.com/watch?v=DgfGNztJUkw
In this video, you will learn how to solve these problems in Python: Intro of Edabit, Pair Management, Boolean to String Conversion, Broken Bridge...
_________
_________
append() Method
https://www.programiz.com/python-programming/methods/list/append
Adds an item to the end of the list.
_________
""" 
# Your code should go here:

def makePair(num1, num2):
    return [num1, num2]

print("The outputs: ")
print(makePair(1, 2))
print(makePair(51, 21))
print(makePair(512124, 215))

print("\nChecking the output type: ")
print(type(makePair(1, 2)))
print(type(makePair(51, 21)))
print(type(makePair(512124, 215)))

# The program is complete.