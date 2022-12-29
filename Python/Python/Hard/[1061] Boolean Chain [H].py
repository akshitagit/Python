"""
####  Boolean Chain  ####

Write three functions:

These functions should evaluate a list of True and False values, starting from the leftmost element and evaluating pairwise.


[Examples]

___
boolean_and([True, True, False, True]) ➞ False
# [True, True, False, True] => [True, False, True] => [False, True] => False

boolean_or([True, True, False, False]) ➞ True
# [True, True, False, True] => [True, False, False] => [True, False] => True

boolean_xor([True, True, False, False]) ➞ False
# [True, True, False, False] => [False, False, False] => [False, False] => False
_____



[Notes]

___
*) XOR is the same as OR, except that it excludes [True, True].
*) Each time you evaluate an element at 0 and at 1, you collapse it into the single result.
___



[arrays] [logic] 



-------------------------------------------------------------------
[Resources]
_________
XOR ( exclusive-OR ) Gate
https://whatis.techtarget.com/definition/logic-gate-AND-OR-XOR-NOT-NAND-NOR-and-XNOR?vgnextfmt=print#xor
Acts in the same way as the logical "either/or." The output is "true" if either, but not both, of the inputs are "true." The output is "false" if both inputs are "false …
_________
_________
logic gate (AND, OR, XOR, NOT, NAND, NOR and XNOR)
https://whatis.techtarget.com/definition/logic-gate-AND-OR-XOR-NOT-NAND-NOR-and-XNOR
A logic gate is an elementary building block of a digital circuit. Most logic gates have two inputs and one output. At any given moment, every terminal is in one of the …
_________
_________
functools reduce() Function
https://www.geeksforgeeks.org/reduce-in-python/
Is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. This function is defined in “functools …
_________
_________
Any All
https://www.geeksforgeeks.org/any-all-in-python/
Are two built ins provided in python used for successive And/Or.
_________
_________
reduce() Function
https://www.geeksforgeeks.org/reduce-in-python/
Is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. This function is defined in “functools …
_________

"""
#Your code should go here:

