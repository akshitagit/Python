"""
##Check if All Values Are True

Create a function that returns True if all parameters are truthy, and False otherwise.


[Examples]

___
all_truthy(True, True, True) ➞ True

all_truthy(True, False, True) ➞ False

all_truthy(5, 4, 3, 2, 1, 0) ➞ False
_____



[Notes]

___
*) Truthy values include non-empty sequences, numbers (except 0 in every numeric type), and basically every value that is not falsy.
*) You can check if an item is truthy by using an if statement on that item.
*) You will always be supplied with at least one parameter.
___



[arrays] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
all() Function
https://www.w3schools.com/python/ref_func_all.asp
Returns True if all items in an iterable are true, otherwise it returns False.
_________
_________
Counting the Number of True Booleans
https://stackoverflow.com/questions/12765833/counting-the-number-of-true-booleans-in-a-python-list
I am looking for a way to count the number of True in the list (so in the example above, I want the return to be 3.) I have found examples of looking for the number of …
_________
_________
*args
https://www.programiz.com/python-programming/args-and-kwargs#:~:text=Python%20has%20*args%20which%20allow,to%20pass%20variable%20length%20arguments.
In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols: *args (Non Keyword Arguments) **kwargs (Keywo …
_________
""" 
# Your code should go here:

allTrue = lambda *inputs : True if all(inputs) == True else False

print(allTrue(True, True, True))
print(allTrue(1, 1, 1, 1, 1, 1))
print(allTrue(1, 0, 1, 1, 1))
print(allTrue(True, False, True))
print(allTrue(5, 4, 3, 2, 1, 0))

# The program is complete.
