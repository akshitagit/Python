"""
####  How Many Rectangles?  ####

Let there be a square matrix, where each square is a rectangle, and a combination of more squares are also rectangles. To find the number of rectangles, Pete sat down and started counting... but that's highly inefficient.
Create a function that takes the order of the matrix as input and returns the number of rectangles in them.


[Examples]

___
rectangles(1) ➞ 1

rectangles(2) ➞ 9

rectangles(3) ➞ 36
_____



[Notes]

___
*) The input will always be an integer.
*) Number of rectangles are given by: ((n(n+1))/2)^2
*) Watch the video listed in the Resources tab to get three different formulas.
___



[algorithms] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Math for fun, how many rectangles?
https://www.youtube.com/watch?v=Uq9OXC0Gzgw
How many rectangles are there in a 8x8 chess board? A combinatoric problem, find the pattern, discrete math problem, number of rectangles on a checker board.
_________
_________
Chess Board: How to Find the Number of Squares and Rectangles
https://mba.hitbullseye.com/CAT/Chess-Puzzles.php
We all have encountered a frequently asked question, "How many squares are there in a 8*8 chessboard?". We usually think the answer is 8*8=64, right? But in this case w …
_________
_________
Number of Rectangles in N*N Grid
https://www.geeksforgeeks.org/number-rectangles-nm-grid/#:~:text=If%20the%20grid%20is%201%C3%971%2C%20there%20is%201%20rectangle.&text=If%20it%20grid%20is%203,2%20%2B%201%20%3D%206%20rectangles.&text=If%20we%20add%20one%20more,of%202%C3%97M%20rectangles.
If the grid is 1×1, there is 1 rectangle. If the grid is 2×1, there will be 2 + 1 = 3 rectangles If it grid is 3×1, there will be 3 + 2 + 1 = 6 rectangles. we can say t …
_________

"""
#Your code should go here:

