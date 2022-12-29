"""
##Maximum Edge of a Triangle

Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.


[Examples]

___
next_edge(8, 10) ➞ 17

next_edge(5, 7) ➞ 11

next_edge(9, 2) ➞ 10
_____



[Notes]

___
*) (side1 + side2) - 1 = maximum range of third edge.
*) The side lengths of the triangle are positive integers.
*) Don't forget to return the result.
___



[algorithms] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Triangle Inequality
https://en.wikipedia.org/wiki/Triangle_inequality
This explains the math behind the triangle inequality.
_________
_________
Find Possible Lengths of Third Side in a Triangle
https://www.youtube.com/watch?v=VW0UM88eLYY
Learn how to find the interval of possible lengths of the third side in a triangle given the two other sides in this free math video tutorial by Mario's Math ...
_________
_________
Python's Basic Operators
https://www.tutorialspoint.com/python/python_basic_operators.htm
Operators are the constructs which can manipulate the value of operands. Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.
_________
_________
Pythagorean Theorem
http://mathworld.wolfram.com/PythagoreanTheorem.html
Many different proofs exist for this most fundamental of all geometric theorems. The theorem can also be generalized from a plane triangle to a trirectangular tetrahedr …
_________
_________
Minimum and Maximum Possible Length of the Third Side of a Triangle
https://www.geeksforgeeks.org/minimum-and-maximum-possible-length-of-the-third-side-of-a-triangle/
Given two sides of a triangle s1 and s2, the task is to find the minimum and maximum possible length of the third side of the given triangle. Print -1 if it is not poss …
_________
_________
How many ways are there to prove the Pythagorean theorem?
https://youtu.be/YompsDlEdtc
What do Euclid, 12-year-old Einstein, and American President James Garfield have in common? They all came up with elegant proofs for the famous Pythagorean theorem, one …
_________
""" 
# Your code should go here:

def thirdEdge(side1, side2):
    if side1 > 0 and side2 > 0:
        return ((side1 + side2)-1)
    else:
        return "Zero and negative inputs not allowed."

print(thirdEdge(8,10))
print(thirdEdge(5,7))
print(thirdEdge(9,2))
print(thirdEdge(0,-3))

# The program is complete.