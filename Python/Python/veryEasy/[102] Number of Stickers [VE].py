"""
##Number of Stickers

Given a Rubik's Cube with a side length of n, return the number of individual stickers that are needed to cover the whole cube.

___
*) The Rubik's cube of side length 1 has 6 stickers.
*) The Rubik's cube of side length 2 has 24 stickers.
*) The Rubik's cube of side length 3 has 54 stickers.
___



[Examples]

___
how_many_stickers(1) ➞ 6

how_many_stickers(2) ➞ 24

how_many_stickers(3) ➞ 54
_____



[Notes]

___
*) Keep in mind there are six faces to keep track of.
*) Expect only positive whole numbers.
___



[algebra] [math] 



-------------------------------------------------------------------
[Resources]
_________
Rubik's Cube
https://en.wikipedia.org/wiki/Rubik%27s_Cube
Is a 3-D combination puzzle invented in 1974 by Hungarian sculptor and professor of architecture Ernő Rubik. Originally called the Magic Cube, the puzzle was licensed b …
_________
_________
How to Raise Numbers to a Power Using ** Operator
https://kodify.net/python/math/exponents/
How to use ** power operators in python, Example (4**2 = 16) because 4 to the power of 2 is 16.
_________
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
""" 
# Your code should go here:

def reqSticker(nSideLen):
    return (nSideLen ** 2) * 6

reqStickLamb = lambda nSideLen : (nSideLen ** 2) * 6

print("The user declared function: ")
print(reqSticker(1))
print(reqSticker(2))
print(reqSticker(3))

print("\nThe lambda function: ")
print(reqStickLamb(1))
print(reqStickLamb(2))
print(reqStickLamb(3))

# The program is complete.