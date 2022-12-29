"""
####  Fix the Code: Un-Mutating a List  ####

Your friend is trying to write a function to accomplish the following transformations:
___
x = [3, 3, 3, 3, 3, 3, 3]

// Each time x is called, the following results are shown:

change(x, 0)  // [3, 3, 3, 3, 3, 3, 3]
change(x, 1)  // [3, 2, 2, 2, 2, 2, 3]
change(x, 2)  // [3, 2, 1, 1, 1, 2, 3]
change(x, 3)  // [3, 2, 1, 0, 1, 2, 3]
_____

Note: The change() function should not mutate the original list. After each call to the function, the original x should still equal [3, 3, 3, 3, 3, 3, 3].
She comes up with the following code:
___
def change(x, times):
  for i in range(len(x)):
    j = 1
    while j <= times:
      if i >= j and i < len(x)-j:
        x[i] -= 1
      j += 1
  return x
_____

Oops! The code appears to mutate the original list. Fix this incorrect code so that the function no longer mutates the original list.
See below:


[Examples]

___
x = [3, 3, 3, 3, 3, 3, 3]

// What we want:
change(x, 2) => [3, 2, 1, 1, 1, 2, 3]

change(x, 2) => [3, 2, 1, 1, 1, 2, 3]

// What we get:
change(x, 2) => [3, 2, 1, 1, 1, 2, 3]  // Good so far...

change(x, 2) => [3, 1, -1, -1, -1, 1, 3] // List is mutated :(
_____



[Notes]

___
*) If this is confusing, copy and paste the incorrect code in a REPL environment and play around with the code to understand what the function is doing.
*) Hint: Try to make a copy of the input list.
*) If this looks familiar, it is part of a solution for the Concentric Rug problem.
___



[bugs] [loops] [scope] 



-------------------------------------------------------------------
[Resources]
_________
copy() Method
https://www.programiz.com/python-programming/methods/list/copy
Returns a shallow copy of the list.
_________
_________
How to Copy a List in Python
https://careerkarma.com/blog/python-copy-list/
o copy a list in Python the copy() function is used. One can also copy a list in Python using slicing, list comprehension, and the list() method. All four methods are u …
_________

"""
#Your code should go here:

