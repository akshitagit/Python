"""
####  Stalactites or Stalagmites?  ####

Stalactites hang from the ceiling of a cave while stalagmites grow from the floor.
Create a function that determines whether the input represents "stalactites" or "stalagmites". If it represents both, return "both". Input will be a 2D list, with 1 representing a piece of rock, and 0 representing air space.


[Examples]

___
mineral_formation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
]) ➞ "stalactites"

mineral_formation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "stalagmites"

mineral_formation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "both"
_____



[Notes]

___
*) There won't be any examples where both stalactites and stalagmites meet (because those are called pillars).
*) There won't be any example of neither stalactites or stalagmites.
*) In other words, if the first list has 1s, return "stalactites". If the last list has 1s, return "stalagmites". If both have them, return "both".
___



[arrays] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Python any() Function
https://beginnersbook.com/2019/03/python-any-function/
Accepts iterable (list, tuple, dictionary etc.) as an argument and return true if any of the element in iterable is true, else it returns false. If iterable is empty th …
_________
_________
sum() Method
https://www.w3schools.com/python/ref_func_sum.asp
Returns a number, the sum of all items in an iterable.
_________

"""
#Your code should go here:

