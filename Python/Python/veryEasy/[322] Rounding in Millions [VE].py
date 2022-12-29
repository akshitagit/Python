"""
##Rounding in Millions

Given a list of cities and populations, return a list where all populations are rounded to the nearest million.


[Examples]

___
millions_rounding([
  ["Nice", 942208],
  ["Abu Dhabi", 1482816],
  ["Naples", 2186853],
  ["Vatican City", 572]
])
_____

___
[
  ["Nice", 1000000],
  ["Abu Dhabi", 1000000],
  ["Naples", 2000000],
  ["Vatican City", 0]
]
_____



[Notes]

Round down to 0 if a population is below 500,000.


[language_fundamentals] [loops] [math] [numbers] [objects] 



-------------------------------------------------------------------
[Resources]
_________
How to round numbers to the nearest 1000?
https://stackoverflow.com/questions/46481351/how-to-round-numbers-to-the-nearest-1000?rq=1
The round function can take negative digits to round to, which causes it to round off to the left of the decimal. I would like to round the list to the nearest 1000. Ho …
_________
_________
round() Method
https://www.w3schools.com/python/ref_func_round.asp
Returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
_________
""" 
# Your code should go here:

