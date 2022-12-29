"""
##Moving House

I'd like to calculate how long on average I've lived in the same house.
Given a person's age and the number of times they've moved house as moves, return the average number of years that they've spent living in the same house.


[Examples]

___
years_in_one_house(30, 1) ➞ 15

years_in_one_house(15, 2) ➞ 5

years_in_one_house(80, 0) ➞ 80
_____



[Notes]

___
*) You can assume that the tests include people who've always lived in a house.
*) Round to the nearest year.
___



[language_fundamentals] [math] 



-------------------------------------------------------------------
[Resources]
_________
round() Method
https://www.w3schools.com/python/ref_func_round.asp
Returns a floating point number that is a rounded version of the specified number, with the specified number of decimals. The default number of decimals is 0, meaning …
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Used to perform operations on variables and values.
_________
_________
Python Logical Operators with Examples
https://www.geeksforgeeks.org/python-logical-operators-with-examples-improvement-needed/
Operators are used to perform operations on values and variables. These are the special symbols that carry out arithmetic and logical computations. The value the operat …
_________
""" 
# Your code should go here:
avgYearsInHouses = lambda age, moves: round(age/(moves+1))

print(avgYearsInHouses(30, 1))
print(avgYearsInHouses(15, 2))
print(avgYearsInHouses(80, 0))
print(avgYearsInHouses(22,1))

# This program is complete.