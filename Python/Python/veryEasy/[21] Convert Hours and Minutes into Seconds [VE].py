"""
##Convert Hours and Minutes into Seconds

Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.


[Examples]

___
convert(1, 3) ➞ 3780

convert(2, 0) ➞ 7200

convert(0, 0) ➞ 0
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[language_fundamentals] [math] 



-------------------------------------------------------------------
[Resources]
_________
How to Do Math in Python with Operators
https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators
Numbers are extremely common in programming. They are used to represent things like screen size dimensions, geographic locations, money and points, the amount of time t …
_________
_________
Convert Hours to Minutes
https://www.calculateme.com/time/hours/to-minutes/
How many minutes are in an hour? Easy hr to min conversion.
_________
_________
How Many Seconds Are In An Hour?
https://www.calculatorology.com/how-many-seconds-are-in-an-hour/
How many seconds are in an hour? Since one hour has 3,600 seconds, the simplest method is to divide the number of seconds by 3,600.
_________
_________
Time to Decimal Calculator
https://www.calculatorsoup.com/calculators/time/time-to-decimal-calculator.php
Convert time hh:mm:ss to decimal hours, decimal minutes and total seconds. Shows steps to calculate decimal hours, minutes and seconds. Conversion calculator that retu …
_________
""" 
# Your code should go here:

def hrMinToSecAdd(hours, minutes):
    return ((hours * (60 ** 2)) + (minutes * 60))

print(hrMinToSecAdd(1, 3))
print(hrMinToSecAdd(2, 0))
print(hrMinToSecAdd(0, 0))
print(hrMinToSecAdd(10,10))

# The program is complete.