"""
##Basic Calculator

Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.


[Examples]

___
calculator(2, "+", 2) ➞ 4

calculator(2, "*", 2) ➞ 4

calculator(4, "/", 2) ➞ 2
_____



[Notes]

If the input tries to divide by 0, return: "Can't divide by 0!"


[algebra] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Python Basic Operators
https://www.tutorialspoint.com/python/python_basic_operators
Operators are the constructs which can manipulate the value of operands. Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.
_________
_________
What does Python's eval() do?
https://stackoverflow.com/questions/9383740/what-does-pythons-eval-do
In the book that I am reading on Python, it keeps using the code eval(input('blah')) I read the documentation, and I understand it, but I still do not see how it chang …
_________
_________
eval() Method
https://www.programiz.com/python-programming/methods/built-in/eval
Parses the expression passed to this method and runs python expression (code) within the program.
_________
_________
Try Except
https://www.w3schools.com/python/python_try_except.asp
Whenever an exception occurs, Python will normally stop and generate an error message. These exceptions can be handled using the try statement.
_________
_________
Python Operators: Arithmetic, Comparison, Logical and More
https://www.programiz.com/python-programming/operators
In this tutorial, you'll learn everything about different types of operators in Python, their syntax and how to use them with examples.
_________
_________
Python Operators
https://www.geeksforgeeks.org/python-operators/
Operators in general are used to perform operations on values and variables in Python. These are standard symbols used for the purpose of logical and arithmetic operati …
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Operators are used to perform operations on variables and values. In the example below, we use the + operator to add together two values.
_________
""" 
# Your code should go here:

def calculator(num1, operator, num2):
    if (num1 == 0 or num2 == 0) and operator == "/":
        return "Can't divide by 0!"
    else:
        match operator:
            case "/" :
                return eval('num1 / num2')
            case "+" :
                return eval('num1 + num2')
            case "*" :
                return eval('num1 * num2')

print(calculator(2, "+", 2))
print(calculator(2, "*", 2))
print(calculator(4, "/", 2))
print(calculator(0, "+", 9))
print(calculator(0, "/", 8))

# The program is complete.