"""
####  Flash Cards  ####

Create a function that outputs the results of a flashcard. A flashcard is a list of three elements: a number, an operator symbol, and another number. Return the mathematical result of that expression.
There are 4 operators: + (addition), - (subtraction), x (multiplication), and / (division). If the flashcard displays a number being divided by zero, e.g. [3, "/", 0], then return None. For division, round to the hundredths place. So [10, "/", 3] should return 3.33.


[Examples]

___
flash([3, "x", 7]) ➞ 21

flash([5, "+", 7]) ➞ 12

flash([10, "-", 9]) ➞ 1

flash([10, "/", 0]) ➞ None

flash([10, "/", 3]) ➞ 3.33
_____



[Notes]

Flash cards contain only zero or positive numbers.


[arrays] [conditions] 



-------------------------------------------------------------------
[Resources]
_________
Turn string into operator?
https://stackoverflow.com/questions/1740726/turn-string-into-operator
How can I turn a string such as "+" into the operator plus? Thanks!
_________
_________
join() Method
https://www.geeksforgeeks.org/join-function-python/
Is a string method and returns a string in which the elements of sequence have been joined by str separator.
_________
_________
round() Method
https://www.programiz.com/python-programming/methods/built-in/round
Returns the floating point number rounded off to the given ndigits digits after the decimal point. If no ndigits is provided, it rounds off the number to the nearest in …
_________
_________
Try Except
https://www.w3schools.com/python/python_try_except.asp
You can define as many exception blocks as you want, e.g. if you want to execute a  special block of code for a special kind of error:
_________
_________
eval() Function
https://www.w3schools.com/python/ref_func_eval.asp
Evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
_________

"""
#Your code should go here:

