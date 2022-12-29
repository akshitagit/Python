"""
##Destructuring Assignment

You can assign variables from lists like this:
___
lst = [1, 2, 3, 4, 5, 6, 7, 8]
first = lst[0]
second = lst[1]
third = lst[2]
other = lst[3:]

print(first) ➞ outputs 1
print(second) ➞ outputs 2
print(third) ➞ outputs 3
print(other) ➞ outputs [4, 5, 6, 7, 8]
_____

Create variables first, second, third and other from the given list using Destructuring Assignment (check the Resources tab for some examples).


[Examples]

___
first ➞ 1

second ➞ 2

third ➞ 3

other ➞ [4, 5, 6, 7, 8]
_____

Your task is to unpack the list writeyourcodehere into four variables, first, second, third, and other.


[Notes]

___
*) Your solution should be just One Line code.
*) If your solution is longer than one line of code, please check the Resources tab.
*) Another version of this challenge.
___



[interview] [language_fundamentals] [logic] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Destructuring Assignment
https://riptutorial.com/python/example/14981/destructuring-assignment
In assignments, you can split an Iterable into values using the "unpacking" syntax.
_________
_________
Destructuring in Python
https://blog.tecladocode.com/destructuring-in-python/
Python, like many programming languages, allows us to assign more than one variable at a time on a single line. We just have to provide the same number of values on bot …
_________
""" 
# Your code should go here:

list1 = range(1, 10+1)
first, second, thrid, *other = list1

print(first)
print(second)
print(thrid)
print(other)

# The program is complete.