"""
##Buggy Code (Part 5)

Mubashir created an infinite loop! Help him by fixing the code in the code tab to pass this challenge. Look at the examples below to get an idea of what the function should do.


[Examples]

___
print_list(1) ➞ [1]

print_list(3) ➞ [1, 2, 3]

print_list(6) ➞ [1, 2, 3, 4, 5, 6]
_____



[Notes]

___
*) READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!
*) Don't overthink this challenge; it's not supposed to be hard.
___



[bugs] [data_structures] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
While Loops
https://www.w3schools.com/python/python_while_loops.asp
With the while loop we can execute a set of statements as long as a condition is true.
_________
_________
Basic Operators
https://www.tutorialspoint.com/python/python_basic_operators.htm
Operators are the constructs which can manipulate the value of operands. Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.
_________
_________
For Loops
https://wiki.python.org/moin/ForLoop
Traditionally used when you have a block of code which you want to repeat a fixed number of times. The Python for statement iterates over the members of a sequence in o …
_________
_________
Loops
https://www.geeksforgeeks.org/loops-in-python/?ref=gcse
Python programming language provides the following types of loops to handle looping requirements. Python provides three ways for executing the loops. While all the ways …
_________
""" 
# Your code should go here:

def listPrint(nth):
    listedView = []
    for i in range(1, nth+1):
        listedView.append(i)
    return listedView

print(listPrint(1))
print(listPrint(3))
print(listPrint(6))

# The program is complete.