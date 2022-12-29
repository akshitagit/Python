"""
##Buggy Code (Part 1)

Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to get an idea of what the function should do.


[Examples]

___
cubes(3) ➞ 27

cubes(5) ➞ 125

cubes(10) ➞ 1000
_____



[Notes]

___
*) READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!
*) Don't overthink this challenge; it's not supposed to be hard.
___



[bugs] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
pow() Function
https://www.w3schools.com/python/ref_func_pow.asp#:~:text=The%20pow()%20function%20returns,power%20of%20y%2C%20modulus%20z.
Return the value of 4 to the power of 3 (same as 4 * 4 * 4).
_________
_________
Cube Numbers
https://www.bbc.co.uk/bitesize/topics/zyhs7p3/articles/z2ndsrd#:~:text=A%20cube%20number%20is%20a,symbol%20for%20cubed%20is%20%C2%B3.
Is a number multiplied by itself 3 times. This can also be called 'a number cubed'. The symbol for cubed is ³.
_________
_________
The Return Statement
https://docs.python.org/2.0/ref/return.html
May only occur syntactically nested in a function definition, not within a nested class definition. If an expression list is present, it is evaluated, else None is sub …
_________
_________
Arithmetic Operators
https://www.w3schools.com/python/python_operators.asp
Are used with numeric values to perform common mathematical operations.
_________
_________
Cube Sum of First N Natural Numbers
https://www.geeksforgeeks.org/python-program-for-program-for-cube-sum-of-first-n-natural-numbers/
Print the sum of series 13 + 23 + 33 + 43 + …….+ n3 till n-th term.
_________
_________
Operators
https://www.w3schools.com/python/python_operators.asp
Are used to perform operations on variables and values. In the example below, we use the + operator to add together two values...
_________
""" 
# Your code should go here:

def cubes(input1):
    return (input1 ** 3)

print(cubes(3))
print(cubes(5))
print(cubes(10))

# The program is complete.
