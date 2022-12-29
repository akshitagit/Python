"""
##Burrrrrrrp

Create a function that returns the string "Burp" with the amount of "r's" determined by the input parameters of the function.


[Examples]

___
long_burp(3) ➞ "Burrrp"

long_burp(5) ➞ "Burrrrrp"

long_burp(9) ➞ "Burrrrrrrrrp"
_____



[Notes]

___
*) Expect num to always be >= 1.
*) Remember to use a capital "B".
*) Don't forget to return the result.
___



[math] [strings] 



-------------------------------------------------------------------
[Resources]
_________
format() Method
https://www.w3schools.com/python/ref_string_format.asp
The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.
_________
_________
Repeat String in Python
https://www.w3schools.in/python-tutorial/repeat-string-in-python/
Sometimes we need to repeat the string in the program, and we can do this easily by using the repetition operator in Python. The repetition operator is denoted by a '*' …
_________
_________
How to Use Python to Multiply Strings
https://www.pythoncentral.io/use-python-multiply-strings/
Did you know that Python can be used to multiply things other than numbers? In fact, you can use Python to multiply strings, which is actually pretty cool when you thin …
_________
_________
String Formatting Best Practices
https://realpython.com/python-string-formatting/
Learn the four main approaches to string formatting in Python, as well as their strengths and weaknesses. You'll also get a simple rule of thumb for how to pick the bes …
_________
_________
join() Function
https://www.w3schools.com/python/ref_string_join.asp
Can be used to concentrate many strings into one.
_________
_________
format() Method
https://www.geeksforgeeks.org/python-string-format-method/?ref=gcse
Has been introduced for handling complex string formatting more efficiently. This method of the built-in string class provides functionality for complex variable substi …
_________
""" 
# Your code should go here:

rBurp = lambda instances : "Bu{}p".format((instances * "r")) if instances >= 1 else "Please input instances of r more than 1."
print(rBurp(2))
print(rBurp(3))
print(rBurp(0))
print(rBurp(5))
print(rBurp(9))

# The program is complete.