"""
####  Letter Distance  ####

Given two words, the letter distance is calculated by taking the absolute value of the difference in character codes and summing up the difference.
If one word is longer than another, add the difference in lengths towards the score.
To illustrate:
___
letter_distance("house", "fly") = dist("h", "f") + dist("o", "l") + dist("u", "y") + dist(house.length, fly.length)

= |104 - 102| + |111 - 108| + |117 - 121| + |5 - 3|
= 2 + 3 + 4 + 2
= 11
_____



[Examples]

___
letter_distance("sharp", "sharq") ➞ 1

letter_distance("abcde", "Abcde") ➞ 32

letter_distance("abcde", "bcdef") ➞ 5
_____



[Notes]

___
*) Always start comparing the two strings from their first letter.
*) Excess letters are not counted towards distance.
*) Capital letters are included.
___



[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
abs() Method
https://www.programiz.com/python-programming/methods/built-in/abs
Returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.
_________
_________
zip() Method
https://www.programiz.com/python-programming/methods/built-in/zip
Take iterables (can be zero or more), makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples.
_________
_________
ord() Method
https://www.programiz.com/python-programming/methods/built-in/ord
Returns an integer representing the Unicode character.
_________
_________
range() Method
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________
_________
len() Method
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________

"""
#Your code should go here:

