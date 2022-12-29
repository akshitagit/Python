"""
####  Explosion Intensity  ####

Given a number, return a string of the word "Boom", which varies in the following ways:
___
*) The string should include n number of "o"s, unless n is below 2 (in that case, return "boom").
*) If n is evenly divisible by 2, add an exclamation mark to the end.
*) If n is evenly divisible by 5, return the string in ALL CAPS.
___

The example below should help clarify these instructions.


[Examples]

___
boom_intensity(4) ➞ "Boooom!"
# There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)

boom_intensity(1) ➞ "boom"
# 1 is lower than 2, so we return "boom"

boom_intensity(5) ➞ "BOOOOOM"
# There are 5 "o"s and 5 is divisible by 5 (all caps)

boom_intensity(10) ➞ "BOOOOOOOOOOM!"
# There are 10 "o"s and 10 is divisible by 2 and 5 (all caps and exclamation mark included)
_____



[Notes]

___
*) A number which is evenly divisible by 2 and 5 will have both effects applied (see example #4).
*) "Boom" will always start with a capital "B", except when n is less than 2, then return a minature explosion as "boom".
___



[algorithms] [formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Repeat String in Python
https://www.w3schools.in/python-tutorial/repeat-string-in-python/
Sometimes we need to repeat the string in the program, and we can do this easily by using the repetition operator in Python. The repetition operator is denoted by a '*' …
_________
_________
Python Ternary Operator
https://data-flair.training/blogs/python-ternary-operator/
Are terse conditional expressions. These are operators that test a condition and based on that, evaluate a value. This was made available since PEP 308 was approved and …
_________

"""
#Your code should go here:

