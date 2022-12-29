"""
##A Day at the Market

Backpack Bill and Wallet Will set off for the annual festival. As they approach the stalls, Bill retorts that he'll be able to bring home more stuff than Will. Taking this as a challenge, Will refutes and a competition spurs into action.
___
*) Backpack Bill has an infinite inventory space, but a limited number of coins.
*) Wallet Will has an infinite number of coins, but a limited inventory space.
___

Create a function that returns the name of the man who can bring home the most items. The parameters are given as follows:



[Worked Example]

___
who_wins_tonight(40, 95, 5, 10) ➞ "Will"

# The item costs 5 coins and takes up 10 inventory spaces.
# Bill can only buy a maximum of 8 items (40 coins DIV 5 = 8).
# Will can only bring home a maximum of 9 items. (95 inventory spaces DIV 10 = 9).
# Will is the winner.
_____



[Examples]

___
who_wins_tonight(20, 20, 5, 10) ➞ "Bill"

who_wins_tonight(10, 2, 20, 1) ➞ "Will"

who_wins_tonight(3, 7, 2, 5) ➞ "Tie"
_____



[Notes]

___
*) DIV means a floored division. That means you round down after dividing.
*) Return "Tie" if both men can afford the same amount of stuff.
*) All numbers will be positive integers.
___



[conditions] [logic] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How to round values up and down?
https://kodify.net/python/math/round-integers/#round-values-up-and-down-pythons-round-function
To round floating-point values up and down we use Python's round() function (Lutz, 2013; Python Docs, n.d. a). There are two ways to use this function. The first option …
_________
_________
How to Round Down in Python
https://www.kite.com/python/answers/how-to-round-down-in-python
Rounding down to the nearest integer results in the closest integer less than or equal to that number. For example, 1.7 rounds down to 1.
_________
""" 
# Your code should go here:

