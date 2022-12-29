"""
##Inches to Feet

Create a function that accepts a measurement value in inches and returns the equivalent of the measurement value in feet.


[Examples]

___
inches_to_feet(324) ➞ 27

inches_to_feet(12) ➞ 1

inches_to_feet(36) ➞ 3
_____



[Notes]

___
*) If inches are under 12, return 0.
*) 12 inches = 1 foot.
___



[language_fundamentals] [math] 



-------------------------------------------------------------------
[Resources]
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Operators are used to perform operations on variables and values.
_________
_________
3 Ways to Convert Inches to Feet
https://www.wikihow.com/Convert-Inches-to-Feet
Converting inches to feet is quick and easy once you know how to do it! The basics to remember are that there are 12 inches in one foot, so you can get from inches to ft …
_________
""" 
# Your code should go here:

inchesToFts = lambda inches : inches/12 if inches >= 12 else 0

print(inchesToFts(324))
print(inchesToFts(12))
print(inchesToFts(36))
print(inchesToFts(11))
print(inchesToFts(5))

# The program is complete.