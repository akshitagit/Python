"""
##Is the Number Even or Odd?

Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers.


[Examples]

___
isEvenOrOdd(3) ➞ "odd"

isEvenOrOdd(146) ➞ "even"

isEvenOrOdd(19) ➞ "odd"
_____



[Notes]

___
*) Dont forget to return the result.
*) Input will always be a valid integer.
*) Expect negative integers (whole numbers).
*) Tests are case sensitive (return "even" or "odd" in lowercase).
___



[conditions] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Check If a Number Is Odd or Even
https://stackoverflow.com/questions/21837208/check-if-a-number-is-odd-or-even-in-python/21837292
I'm trying to make a program which checks if a word is a palindrome and I've gotten so far and it works with words that have an even amount of numbers. I know how to ma …
_________
_________
Python Operators: Arithmetic Comparison Logical and More
https://www.programiz.com/python-programming/operators
In this article, you'll learn everything about different types of operators in Python, their syntax and how to use them with examples.
_________
_________
Remainder - Arithmetic Operators
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators#Remainder_()
Returns the remainder left over when one operand is divided by a second operand. It always takes the sign of the dividend.
_________
_________
What is an even or an odd number?
https://www.mathsisfun.com/numbers/even-odd.html
Even: Any integer that can be divided exactly by 2 is an even number. Odd: Any integer that cannot be divided exactly by 2 is an odd number.
_________
_________
Conditional Expressions
https://docs.python.org/2.5/whatsnew/pep-308.html
For a long time, people have been requesting a way to write conditional expressions, which are expressions that return value A or value B depending on whether a Boolean …
_________
""" 
# Your code should go here:

checkEvenOdd = lambda int1 : "even" if int1 % 2 == 0 else "odd"

print(checkEvenOdd(3))
print(checkEvenOdd(146))
print(checkEvenOdd(19))
print(checkEvenOdd(-12))
print(checkEvenOdd(-121))

# The program is complete.
