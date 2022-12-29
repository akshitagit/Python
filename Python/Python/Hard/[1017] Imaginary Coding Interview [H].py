"""
####  Imaginary Coding Interview  ####

Create a function to check if a candidate is qualified in an imaginary coding interview of an imaginary tech startup.
The criteria for a candidate to be qualified in the coding interview is:

If all the above conditions are satisfied, return "qualified", else return "disqualified".
You will be given a list of time taken by a candidate to solve a particular question and the total time taken by the candidate to complete the interview.
Given a list , in a true condition will always be in the format [very easy, very easy, easy, easy, medium, medium, hard, hard].
The maximum time to complete the interview includes a buffer time of 20 minutes.


[Examples]

___
interview([5, 5, 10, 10, 15, 15, 20, 20], 120) ➞ "qualified"

interview([2, 3, 8, 6, 5, 12, 10, 18], 64) ➞  "qualified"

interview([5, 5, 10, 10, 25, 15, 20, 20], 120) ➞ "disqualified"
# Exceeded the time limit for a medium question.

interview([5, 5, 10, 10, 15, 15, 20], 120) ➞ "disqualified"
# Did not complete all the questions.

interview([5, 5, 10, 10, 15, 15, 20, 20], 130) ➞ "disqualified"
# Solved all the questions in their respected time limits but exceeded the total time limit of the interview.
_____



[Notes]

Try to solve the problem using only list methods.


[arrays] [conditions] [interview] 



-------------------------------------------------------------------
[Resources]
_________
For Loops
https://www.w3schools.com/python/python_for_loops.asp
Used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
_________
_________
If ... Else
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics. These conditions can be used in several ways, most commonly in "if statements" and loops. An "if statem …
_________
_________
zip() Function
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and return it. In this tutorial, we will learn about Python zip() in detail with the help of examples.
_________

"""
#Your code should go here:

