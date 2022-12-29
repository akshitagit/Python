"""
##Calculate Using String Operation

Create a function that takes two numbers and a mathematical operator and returns the result.


[Examples]

___
calculate(4, 9, "+") ➞ 13

calculate(12, 5, "-") ➞ 7

calculate(6, 3, "*") ➞ 18

calculate(25, 5, "//") ➞ 5

calculate(14, 3, "%") ➞ 2

calculate(7, 2, "/") ➞ 3.5
_____



[Notes]

___
*) Numbers can be negative.
*) The only operations used are those in the examples above.
___



[algebra] [math] [strings] 



-------------------------------------------------------------------
[Resources]
_________
eval(): Evaluate Expressions Dynamically
https://realpython.com/python-eval-function/
Allows you to evaluate arbitrary Python expressions from a string-based or compiled-code-based input. This function can be handy when you’re trying to dynamically evalu …
_________
_________
str() Function
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object. In this tutorial, we will learn about Python str() in detail with the help of examples.
_________
_________
"if, elif, else" Statement
https://www.programiz.com/python-programming/if-elif-else
In this article, you will learn to create decisions in a Python program using different forms of if..else statement.
_________
""" 
# Your code should go here:

# calculator = lambda num1, num2, operator1 :eval(str("num1 operator1 num2"))
# def calculator(num1, num2, operator1):
#     return eval(str(num1, operator1, num2))
def calculator(num1, num2, operator1):
    if operator1 == "+":
        return num1 + num2
    elif operator1 == "-":
        return num1 - num2
    elif operator1 == "*":
        return num1 * num2
    elif operator1 == "//":
        return num1 // num2
    elif operator1 == "%":
        return num1 % num2
    elif operator1 == "/":
        return num1 / num2
    else:
        return "Input operator out of scope."

print(calculator(4, 9, "+"))
print(calculator(12, 5, "-"))
print(calculator(6, 3, "*"))
print(calculator(25, 5, "//"))
print(calculator(14, 3, "%"))
print(calculator(7, 2, "/"))

# The program is complete.