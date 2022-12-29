"""
####  Don't Roll Doubles!  ####

John is playing a dice game. The rules are as follows.

But if you roll DOUBLES, your score is instantly wiped to 0 and your game ends immediately!
Create a function that takes in a list of tuples as input, and return John's score after his game has ended.


[Examples]

___
dice_game([(1, 2), (3, 4), (5, 6)]) ➞ 21

dice_game([(1, 1), (5, 6), (6, 4)]) ➞ 0

dice_game([(4, 5), (4, 5), (4, 5)]) ➞ 27
_____



[Notes]

___
*) Ignore all other tuples in the list if a throw happens to be doubles and go straight to returning 0.
*) John only has two dice and will always give you outcomes for three rounds.
___



[algorithms] [arrays] [games] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Adding Two List Elements
https://www.geeksforgeeks.org/python-adding-two-list-elements/
There can be many situations in which one requires to find index wise summation of two different lists. This can have a possible applications in day-day programming. Le …
_________
_________
Break inside List Comprehension
https://stackoverflow.com/questions/45780245/break-inside-list-comprehension/45780315
Use any() with a generator filterList=['test','2','x','123','orange'] print ([i for i in datalist if any(j for j in filterList if j in i) ]) any stops the iterations w …
_________

"""
#Your code should go here:

