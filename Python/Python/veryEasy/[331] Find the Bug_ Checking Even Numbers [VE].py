"""
##Find the Bug: Checking Even Numbers

Create a function that takes in an array and returns True if all its values are even, and False otherwise.
Not a big deal, your friend says. He writes the following code:
___
def check_all_even(lst):
  return all(x % 2 == 0)
_____

The code above leads to a Reference Error, with x being undefined. Fix the code above so that all tests pass:


[Examples]

___
check_all_even([1, 2, 3, 4]) ➞ False

check_all_even([2, 4, 6]) ➞ True

check_all_even([5, 6, 8, 10]) ➞ False

check_all_even([-2, 2, -2, 2]) ➞ True
_____



[Notes]

For help, check Resources or ask a question in the Comments.


[arrays] [bugs] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Looping Over a List in Python
https://stackoverflow.com/questions/9138112/looping-over-a-list-in-python
I have a list with sublists in it. I want to print all the sublists with length equal to 3.
_________
_________
Binary Bitwise Operations
https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations
The & operator yields the bitwise AND of its arguments, which must be integers.
_________
_________
How to check if there's any odd/even numbers in an Iterable (e.g. list/tuple)?
https://stackoverflow.com/questions/44256048/how-to-check-if-theres-any-odd-even-numbers-in-an-iterable-e-g-list-tuple/44256147
Suppose we're checking if there's any odd numbers in a list. The has_odd function checks if there's any odd numbers in a list, once an odd number is found, it returns T …
_________
_________
How do you divide each element in a list by an int?
https://stackoverflow.com/questions/8244915/how-do-you-divide-each-element-in-a-list-by-an-int/8247234
I just want to divide each element in a list by an int. This is the error: TypeError: unsupported operand type(s) for /: 'list' and 'int' I understand why I am receivin …
_________
_________
all() Method
https://www.programiz.com/python-programming/methods/built-in/all
Returns True when all elements in the given iterable are true. If not, it returns False.
_________
_________
Python yield, Generators and Generator Expressions
https://www.programiz.com/python-programming/generator
In this article, you'll learn how to create iterations easily using Python generators, how is it different from iterators and normal functions, and why you should use it.
_________
""" 
# Your code should go here:

