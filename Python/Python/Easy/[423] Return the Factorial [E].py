"""
##Return the Factorial

Create a function that takes an integer and returns the factorial of that integer.
That is, the integer multiplied by all positive lower integers.


[Examples]

___
factorial(3) ➞ 6

factorial(5) ➞ 120

factorial(13) ➞ 6227020800
_____



[Notes]

Assume all inputs are greater than or equal to 0.


[algebra] [math] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
factorial() Method
https://www.geeksforgeeks.org/factorial-in-python/
Not many people know, but python offers a direct function that can compute the factorial of a number without writing the whole code for computing factorial.
_________
_________
Thinking Recursively
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________
_________
factorial() Method
https://www.tutorialspoint.com/factorial-in-python#:~:text=Finding%20the%20factorial%20of%20a,1%20till%20the%20given%20number.
Finding the factorial of a number is a frequent requirement in data analysis and other mathematical analysis involving python. The factorial is always found for a posit …
_________
_________
Factorial with Recursion
https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursive-factorial
Explanation on how to solve factorials using recursion.
_________
_________
Factorial
https://en.wikipedia.org/wiki/Factorial
In mathematics, the factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n.
_________
_________
Recursion
https://www.programiz.com/python-programming/recursion
In this tutorial, you will learn to create a recursive function (a function that calls itself).
_________
_________
How can I multiply all items in a list together with Python?
https://stackoverflow.com/questions/13840379/how-can-i-multiply-all-items-in-a-list-together-with-python
I need to write a function that takes a list of numbers and multiplies them together. Example: [1,2,3,4,5,6] will give me 1*2*3*4*5*6. I could really use your help.
_________
_________
What is Recursion?
https://www.youtube.com/watch?v=k7-N8R0-KY4
A video explaining on what recursion is.
_________
""" 
# Your code should go here:

def factorial(n):
    if n >= 0:
        fact = 1
        i = 1
        while i <= n:
            fact = i * fact
            i = i + 1
        return fact
    else:
        return "n for factorial cannot be less than zero."

def factorialForLoop(n):
    if n >= 0:
        sum = 0
        a = []
        for i in range(1, n+1):
            print(i)
            i = i * 1
            sum = i + sum
            # a.append(i * 1)
        return (i, sum)

print(factorial(3))
print(factorial(5))
print(factorial(13))

print(factorialForLoop(3))
print(factorialForLoop(5))
print(factorialForLoop(13))

# factorial(3) ➞ 6
#
# factorial(5) ➞ 120
#
# factorial(13) ➞ 6227020800
# _____
#
#
#
# [Notes]
#
# Assume all inputs are greater than or equal to 0.
