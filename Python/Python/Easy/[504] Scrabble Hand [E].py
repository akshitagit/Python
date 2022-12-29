"""
##Scrabble Hand

Given a list of scrabble tiles (as dictionaries), create a function that outputs the maximum possible score a player can achieve by summing up the total number of points for all the tiles in their hand. Each hand contains 7 scrabble tiles.
Here's an example hand:
___
[
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]
_____

The player's maximum_score from playing all these tiles would be 1 + 5 + 10 + 8 + 2 + 1 + 1, or 28.


[Examples]

___
maximum_score([
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]) ➞ 28

maximum_score([
  { "tile": "B", "score": 2 },
  { "tile": "V", "score": 4 },
  { "tile": "F", "score": 4 },
  { "tile": "U", "score": 1 },
  { "tile": "D", "score": 2 },
  { "tile": "O", "score": 1 },
  { "tile": "U", "score": 1 }
]) ➞ 15
_____



[Notes]

Here, each tile is represented as an dictionary with two keys: tile and score.


[games] [loops] [math] [objects] 



-------------------------------------------------------------------
[Resources]
_________
get() Method
https://www.w3schools.com/python/ref_dictionary_get.asp
Returns the value of the item with the specified key.
_________
_________
Python Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp
A collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
_________
_________
sum() Method
https://www.w3schools.com/python/ref_func_sum.asp
Returns a number, the sum of all items in an iterable.
_________
""" 
# Your code should go here:

