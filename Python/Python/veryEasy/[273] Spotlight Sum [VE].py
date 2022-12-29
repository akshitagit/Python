"""
##Spotlight Sum

Given a 10x10 grid of numbers 1-100, return the Spotlight Sum, given a number n. The spotlight sum can be defined as the total of the 8 numbers immediately surrounding the number n on the grid, including n in the total.


[Worked Example]

___
[
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
  [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
  [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
  [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
  [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
  [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
  [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
  [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
]

spotlight_sum(45) ➞ 405

# The 8 numbers surrounding 45 on the grid are:
# [34, 35, 36, 44, 46, 54, 55, 56]
# Total of the numbers is 360.
# Include 45 in the total (360 + 45 = 405)
# Return the answer.
_____



[Examples]

___
spotlight_sum(19) ➞ 171

spotlight_sum(48) ➞ 432

spotlight_sum(88) ➞ 792
_____



[Notes]

Note that any numbers which don't have the full 8 numbers surrounding it are not included in the tests.


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
3 Ways to Multiply
https://www.wikihow.com/Multiply
How to Multiply. Multiplication is one of the four basic operations in arithmetic, along with addition, subtraction, and division. Multiplication can actually be consid …
_________
""" 
# Your code should go here:

