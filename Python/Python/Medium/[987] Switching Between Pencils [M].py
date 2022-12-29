"""
####  Switching Between Pencils  ####

When coloring a striped pattern, you may start by coloring each square sequentially, meaning you spend time needing to switch coloring pencils.
Create a function where given a list of colors cols, return how long it takes to color the whole pattern. Note the following times:
___
*) It takes 1 second to switch between pencils.
*) It takes 2 seconds to color a square.
___

See the example below for clarification.
___
color_pattern_times(["Red", "Blue", "Red", "Blue", "Red"]) ➞ 14

# There are 5 colors so it takes 2 seconds to color each one (2 x 5 = 10).
# You need to switch the pencils 4 times and it takes 1 second to switch (1 x 4 = 4).
# 10 + 4 = 14
_____



[Examples]

___
color_pattern_times(["Blue"]) ➞ 2

color_pattern_times(["Red", "Yellow", "Green", "Blue"]) ➞ 11

color_pattern_times(["Blue", "Blue", "Blue", "Red", "Red", "Red"]) ➞ 13
_____



[Notes]

___
*) Only change coloring pencils if the next color is different to the color before it.
*) Return a number in seconds.
___



[algorithms] [arrays] 



-------------------------------------------------------------------
[Resources]
_________
sum() Method
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
range() Method
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________
_________
How to check if previous element is similar to next element?
https://stackoverflow.com/questions/25215494/how-to-check-if-previous-element-is-similar-to-next-elemnt-in-python
You can create a list comprehension and check if the ith element is equal to the ith-1 element in your list. This can be written within a for loop as well.
_________
_________
len() Method
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________

"""
#Your code should go here:

