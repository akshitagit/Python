"""
##Edaaaaabit

Write a function that takes an integer and returns a string with the given number of "a"s in Edabit.


[Examples]

___
how_many_times(5) ➞ "Edaaaaabit"

how_many_times(0) ➞ "Edbit"

how_many_times(12) ➞ "Edaaaaaaaaaaaabit"
_____



[Notes]

___
*) The string must start with "Ed" and end with "bit".
*) You'll only be given integers as test input.
___



[formatting] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
format() Method
https://www.geeksforgeeks.org/python-format-function/
This method lets us concatenate elements within a string through positional formatting.
_________
_________
Using % and .format() for great good!
https://pyformat.info/
Python has had awesome string formatters for many years but the documentation on them is far too theoretic and technical. With this site we try to show you the most com …
_________
_________
Multiplication with Strings
https://www.informit.com/articles/article.aspx?p=2140372&seqNum=4
When you multiply a string by an integer, Python returns a new string. This new string is the original string, repeated X number of times (where X is the value of the i …
_________
""" 
# Your code should go here:

def multipleA(num1):
    a = "a" * round(num1)
    return "Ed{0}bit".format(a)

multipleA1 = lambda num1 : "Ed{0}bit".format(("a" * round(num1)))
print(multipleA(2))
print(multipleA(3))
print(multipleA(1.5))
print(multipleA(-2))
print(multipleA(0))
print("\nLambda equipped method:-")
print(multipleA1(2))
print(multipleA1(3))
print(multipleA1(1.5))
print(multipleA1(-2))
print(multipleA1(0))

# The program is complete.