"""
##Tile Teamwork Tactics

In a board game, a piece may advance 1-6 tiles forward depending on the number rolled on a six-sided dice. If you advance your piece onto the same tile as another player's piece, both of you earn a bonus.
Can you reach your friend's tile number in the next roll? Create a function that returns if it's possible to earn a bonus when you roll the dice.


[Examples]

___
possible_bonus(3, 7) ➞ True

possible_bonus(1, 9) ➞ False

possible_bonus(5, 3) ➞ False
_____



[Notes]

___
*) You cannot move backward (which is why example #3 doesn't work).
*) If you are already on the same tile, return False, as you would be advancing away.
*) Expect only positive integer inputs.
___



[conditions] [language_fundamentals] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
range() Function
https://www.w3schools.com/python/ref_func_range.asp
Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
_________
_________
Operators
https://www.w3schools.com/python/python_operators.asp
Are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
_________
""" 
# Your code should go here:

