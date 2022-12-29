"""
####  Narcissistic Numbers  ####

A number is narcissistic when the sum of its digits, with each digit raised to the power of digits quantity, is equal to the number itself.
___
153 ➞ 3 digits ➞ 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ➞ Narcissistic
84 ➞ 2 digits ➞ 8² + 4² = 64 + 16 = 80 ➞ Not narcissistic
_____

Given a positive integer n, implement a function that returns True if the number is narcissistic, and False if it's not.


[Examples]

___
is_narcissistic(8208) ➞ True
// 8⁴ + 2⁴ + 0⁴ + 8⁴ = 8208

is_narcissistic(22) ➞ False
// 2² + 2² = 8

is_narcissistic(9) ➞ True
// 9¹ = 9
_____



[Notes]

___
*) Trivially, any number in the 1-9 range is narcissistic and any two-digit number is not.
*) Curious fact: Only 88 numbers are narcissistic.
___



[language_fundamentals] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Check whether a given number is a narcissistic number or not?
https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-96.php#:~:text=In%20mathematics%2C%20he%20has%20kins,of%20the%20number%20of%20digits.&text=407%20%3D%2043%20%2B%2003%20%2B%2073.
Write a Python program to check whether a given number is a narcissistic number or not. If you are a reader of Greek mythology, then you are probably familiar with Nar …
_________
_________
str() Function
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object. In this tutorial, we will learn about Python str() in detail with the help of examples.
_________
_________
len() Function
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
_________
Narcissistic Numbers
https://www.geeksforgeeks.org/narcissistic-number/
The approach will be to count the number of digits and then extract every digit and then by using pow function we can get the power of that digit and then sum it up at …
_________
_________
Checking for Narcissism in Numbers (Python)
https://code.likeagirl.io/algorithm-part-1-checking-for-narcissism-of-a-number-python-cbea596b2790
Basically, a narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits it has. P.S: They are also referred to a …
_________

"""
#Your code should go here:

