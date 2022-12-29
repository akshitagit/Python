"""
##Chocolate Dilemma

Two sisters are eating chocolate, whose pieces are represented as subarrays of [l x w].
Write a function that returns True if the total area of chocolate is the same for each sister.
To illustrate:
___
test_fairness([[4, 3], [2, 4], [1, 2]],
[[6, 2], [4, 2], [1, 1], [1, 1]])
➞ True

// Agatha's pieces: [4, 3], [2, 4], [1, 2]
// Bertha's pieces: [6, 2], [4, 2], [1, 1], [1, 1]

// Total area of Agatha's chocolate
// 4x3 + 2x4 + 1x2 = 12 + 8 + 2 = 22

// Total area of Bertha's chocolate is:
// 6x2 + 4x2 + 1x1 + 1x1 = 12 + 8 + 1 + 1 = 22
_____



[Examples]

___
test_fairness([[1, 2], [2, 1]], [[2, 2]]) ➞ true

test_fairness([[1, 2], [2, 1]], [[2, 2], [4, 4]]) ➞ false

test_fairness([[2, 2], [2, 2], [2, 2], [2, 2]], [[4, 4]]) ➞ true

test_fairness([[1, 5], [6, 3], [1, 1]], [[7, 1], [2, 2], [1, 1]]) ➞ false
_____



[Notes]

N/A


[arrays] [conditions] 



-------------------------------------------------------------------
[Resources]
_________
How can I multiply all items in a list together with Python?
https://stackoverflow.com/questions/13840379/how-can-i-multiply-all-items-in-a-list-together-with-python
I need to write a function that takes a list of numbers and multiplies them together. Example: [1,2,3,4,5,6] will give me 1*2*3*4*5*6. I could really use your help.
_________
_________
sum() Method
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum.
_________
_________
reduce() Function
https://thepythonguru.com/python-builtin-functions/reduce/
Accepts a function and a sequence and returns a single value calculated as follows: Initially, the function is called with the…
_________
_________
range() Method
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________
_________
Multiplication of All Elements in Two Lists
https://www.xspdf.com/resolution/52237470.html
How to multiply all integers inside list, Try a list comprehension: l = [x * 2 for x in l]. This goes through l , multiplying each element by two. Of course, there's mo …
_________
""" 
# Your code should go here:

