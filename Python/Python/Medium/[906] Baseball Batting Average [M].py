"""
####  Baseball Batting Average  ####

A baseball player's batting average is calculated by the following formula:
___
BA = (number of hits) / (number of official at-bats)
_____

Batting averages are always expressed rounded to the nearest thousandth with no leading zero. The top 3 MLB batting averages of all-time are:

The given list represents a season of games. Each list item indicates a player's [hits, official at bats] per game. Return a string with the player's seasonal batting average rounded to the nearest thousandth.


[Examples]

___
batting_avg([[0, 0], [1, 3], [2, 2], [0, 4], [1, 5]]) ➞ ".286"

batting_avg([[2, 5], [2, 3], [0, 3], [1, 5], [2, 4]]) ➞ ".350"

batting_avg([[2, 3], [1, 5], [2, 4], [1, 5], [0, 5]]) ➞ ".273"
_____



[Notes]

___
*) The number of hits will not exceed the number of official at-bats.
*) The list includes official at-bats only. No other plate-appearances (walks, hit-by-pitches, sacrifices, etc.) are included in the list.
*) HINT: Think in terms of total hits and total at-bats.
___



[arrays] [formatting] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
round() Function
https://www.w3schools.com/python/ref_func_round.asp
Returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
_________
_________
sum() Function
https://www.w3schools.com/python/ref_func_sum.asp
Returns a number, the sum of all items in an iterable.
_________
_________
ljust() Method
https://www.w3schools.com/python/ref_string_ljust.asp
Will left align the string, using a specified character (space is default) as the fill character.
_________
_________
Unpacking Unspecified Values
https://stackoverflow.com/questions/57814195/what-does-for-x-y-in-list-mean-in-python
Uses the unpacking methods for tuples in combination with *args to unpack an unspecified number of values using iteration.
_________

"""
#Your code should go here:

