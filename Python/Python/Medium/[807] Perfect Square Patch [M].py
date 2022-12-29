"""
####  Perfect Square Patch  ####

Create a function that takes an integer and outputs an n x n square solely consisting of the integer n.


[Examples]

___
square_patch(3) ➞ [
  [3, 3, 3],
  [3, 3, 3],
  [3, 3, 3]
]

square_patch(5) ➞ [
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5]
]

square_patch(1) ➞ [
  [1]
]

square_patch(0) ➞ []
_____



[Notes]

___
*) n >= 0.
*) If n == 0, return an empty list.
___



[arrays] [language_fundamentals] [loops] 



-------------------------------------------------------------------
[Resources]
_________
How to define a two-dimensional list in Python?
https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
I want to define a two-dimensional array without an initialized length like this: Matrix = [][] but it does not work... I've tried the code below, but it is wrong too …
_________
_________
range() Method
https://www.w3schools.com/python/ref_func_range.asp
Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
_________
_________
Generating sublists using multiplication ( * ) unexpected behavior
https://www.semicolonworld.com/question/54184/generating-sublists-using-multiplication-unexpected-behavior
You changed the reference that occupies lst[0]; that is, you assigned a new value to lst[0]. But you didn't change the value of the other elements, they still refer to …
_________
_________
3 Ways To Create a List Repeating an Item
https://cmdlinetips.com/2018/12/3-ways-to-create-a-list-repeating-an-item/
Sometimes, you may want to create a list in Python such that it contains the same element repeated many times. In Python, you can create such a repeat list easily using …
_________

"""
#Your code should go here:

