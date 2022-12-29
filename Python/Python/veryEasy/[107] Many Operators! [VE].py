"""
##Many Operators!

Some basic arithmetic operators are +, -, *, /, and %.
In this challenge you will be given three parameters, num1, num2, and an operator.
Use the operator on number 1 and 2.


[Examples]

___
operate(1, 2, "+") ➞ 3
# 1 + 2 = 3

operate(7, 10, "-") ➞ -3
# 7 - 10 = -3

operate(20, 10, "%") ➞ 0
# 20 % 10 = 0
_____



[Notes]

There will not be any divisions by zero.


[language_fundamentals] [math] 



-------------------------------------------------------------------
[Resources]
_________
eval() Method
https://www.programiz.com/python-programming/methods/built-in/eval
Parses the expression passed to this method and runs python expression (code) within the program.
_________
_________
Python eval(): Evaluate Expressions Dynamically
https://realpython.com/python-eval-function/
In this step-by-step tutorial, you'll learn how Python's eval() works and how to use it effectively in your programs. Additionally, you'll learn how to minimize the sec …
_________
_________
Convert Integer to String
https://www.geeksforgeeks.org/convert-integer-to-string-in-python/
In Python an integer can be converted into a string using the built-in str() function. The str() function takes in any python data type and converts it into a string. B …
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Operators are used to perform operations on variables and values. In the example below, we use the + operator to add together two values.
_________
_________
format() Method
https://www.w3schools.com/python/ref_string_format.asp
Formats the specified value(s) and insert them inside the string's placeholder. The placeholder is defined using curly brackets: {}. Read more about the placeholders i …
_________
""" 
# Your code should go here:

def switchMethod(num1, num2, operator):
    match operator:
        case "+" | "-" | "%":
            return eval("{0}{1}{2}".format(num1, operator, num2))
        case _:
            return "Please enter the operator from the given."

print(switchMethod(1, 2, "-"))
print(switchMethod(2, 2, "+"))
print(switchMethod(3, 3, "%"))
print(switchMethod(10, 5, "-"))
print(switchMethod(103, 10, "%"))

# The program is complete.



# Just test function.
# def matchCaseTest(respCode):
#     match respCode:
#         case 400:
#             return "Hello, 400 is returned."
#         case 401 | 402:
#             return "Hello, 401 and 402 is returned."
#         case 403:
#             return "Hello 403 is returned."
#         case 404:
#             return "Hello 404 is returned."
#         case 405:
#             return "Hello, 405 is returned."
#         case _:
#             return "Yikes, fuck you bitch"
#
# print(matchCaseTest(100))
# print(matchCaseTest(404))
# print(matchCaseTest(401))
# print(matchCaseTest(402))
