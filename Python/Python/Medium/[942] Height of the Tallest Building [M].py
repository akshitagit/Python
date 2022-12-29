"""
####  Height of the Tallest Building  ####

Given a list of strings (depicting a skyline of several buildings), return in meters the height of the tallest building. Each line in the list represents 20m.


[Examples]

___
tallest_building_height([
  "            ##",
  "            ##",
  "            ##",
  "###   ###   ##",
  "###   ###   ###",
  "###   ###   ###",
  "###   ###   ###"
]) ➞ "140m"

# Tallest building is 7 characters
# 7 x 20m = 140m

tallest_building_height([
  "               ",
  "               ",
  "               ",
  "       #    ###",
  "      # #   ###",
  "###   ###   ###",
  "###   ###   ###"
]) ➞ "80m"

# Tallest building is 4 characters
# 4 x 20m = 80m

tallest_building_height([
  "                              ",
  "                         ###  ",
  "                         ###  ",
  "###                    #####  ",
  "###      #             #####  ",
  "###     ###            #####  ",
  "######  ###            #######",
  "######  ######  ###    #######",
  "###################    #######",
  "###############################",
  "###############################"
]) ➞ "200m"

# Tallest building is 10 characters
# 10 x 20m = 200m
_____



[Notes]

___
*) There may be some open sky above buildings (can't just find the length of the list).
*) There may be multiple tallest buildings (see example #2).
___



[algorithms] [arrays] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Enumerate()
https://www.geeksforgeeks.org/enumerate-in-python/
Adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of …
_________
_________
For Loops
https://www.programiz.com/python-programming/for-loop
In this article, you'll learn to iterate over a sequence of elements using the different variations of for loop.
_________
_________
Python if, if...else, if...elif...else and Nested if Statement
https://www.programiz.com/python-programming/if-elif-else
In this article, you will learn to create decisions in a Python program using different forms of if..else statement.
_________

"""
#Your code should go here:

