"""
####  Check If Lines Are Parallel  ####

Given two lines, determine whether or not they are parallel.
Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.


[Examples]

___
lines_are_parallel([1, 2, 3], [1, 2, 4]) ➞ True
# x+2y=3 and x+2y=4 are parallel.

lines_are_parallel([2, 4, 1], [4, 2, 1]) ➞ False
# 2x+4y=1 and 4x+2y=1 are not parallel.

lines_are_parallel([0, 1, 5], [0, 1, 5]) ➞ True
# Lines are parallel to themselves.
_____



[Notes]

___
*) Two lines are parallels if they have the same slope. If the slopes are different, the lines are not parallel.
*) All test cases use valid input (no lists of the wrong size, for example).
*) All coefficients will be integers (whole numbers).
___



[algebra] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Finding Parallel and Perpendicular Lines
https://www.mathsisfun.com/algebra/line-parallel-perpendicular.html
How do we know if they are really the same line? Check their y-intercepts (where they cross the y-axis) as well as their slope.
_________
_________
How to Find out If Lines Are Parallel
https://www.varsitytutors.com/sat_math-help/how-to-find-out-if-lines-are-parallel
y – 2 = ¾x is y = ¾x + 2 in slope intercept form (y=mx + b where m is the slope and b is the y-intercept). In this line, the slope is ¾. Parallel lines have the same …
_________
_________
How to Determine if Lines are Parallel
https://www.youtube.com/watch?v=Lf3KrvnLCug
In this video we define parallel lines, giving a parallel lines definition, on the way to determining if two lines are parallel. The given a line, the slope of a parall …
_________
_________
Given the Equations of Two Lines, Determine Whether Their Graphs Are Parallel or Perpendicula
https://courses.lumenlearning.com/collegealgebra1/chapter/given-the-equations-of-two-lines-determine-whether-their-graphs-are-parallel-or-perpendicular/
We can determine from their equations whether two lines are parallel by comparing their slopes. If the slopes are the same and the y-intercepts are different, the lines …
_________
_________
Python Program to Check If Two Lines Are Parallel or Not
https://www.codespeedy.com/python-program-to-check-if-two-lines-are-parallel-or-not/
In this post, we will try to code a Python program to check if two lines are parallel or not. So what are parallel lines? Two lines are said to be parallel if they rema …
_________
_________
General Equation of a Line
https://www.youtube.com/watch?v=LxNB7iSaaco
Ax + By + C = 0 Slope – intercept form Intercept form Normal form. We are already familiar about the straight Lines concept however what we know from the previous class …
_________
_________
Parallel lines from equation
https://www.khanacademy.org/math/geometry/hs-geo-analytic-geometry/hs-geo-parallel-perpendicular-eq/v/parallel-lines-3
We're asked which of these lines are parallel. So they give us three equations of three different lines and if they're parallel, then they have to have the same slope. …
_________
_________
Parallel Lines
https://www.montereyinstitute.org/courses/Algebra1/COURSE_TEXT_RESOURCE/U04_L2_T1_text_final.html
Parallel lines are two or more lines that never intersect. Examples of parallel lines are all around us, in the two sides of this page and in the shelves of a bookcase. …
_________
_________
Check Whether Two Given Lines Are Parallel or Not
https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-103.php
Parallel lines are two or more lines that never intersect. Parallel Lines are like railroad tracks that never intersect. The General Form of the equation of a straight …
_________
_________
How To Tell If Two Lines Are Parallel, Perpendicular, or Neither?
https://www.youtube.com/watch?v=Uq8pSFaXPmQ
This algebra video tutorial explains how to tell if two lines are parallel, perpendicular, or neither. It gives you a few examples and practice problems.
_________

"""
#Your code should go here:

