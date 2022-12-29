"""
##Name Greeting!

Create a function that takes a name and returns a greeting in the form of a string.


[Examples]

___
hello_name("Gerald") ➞ "Hello Gerald!"

hello_name("Tiffany") ➞ "Hello Tiffany!"

hello_name("Ed") ➞ "Hello Ed!"
_____



[Notes]

___
*) The input is always a name (as string).
*) Don't forget the exclamation mark!
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[formatting] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python String Formatting Best Practices
https://realpython.com/python-string-formatting/
In this tutorial, you’ll learn the four main approaches to string formatting in Python, as well as their strengths and weaknesses. You’ll also get a simple rule of thum …
_________
_________
String Concatenation and Formatting
https://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python
One common task you’ll need to accomplish with any language involves merging or combining strings. This process is referred to as concatenation. The best way to describ …
_________
_________
Strings
https://www.w3schools.com/python/python_strings.asp
String literals in python are surrounded by either single quotation marks, or double quotation marks. 'hello' is the same as "hello". You can display a string literal …
_________
_________
Python 3's f-Strings
https://realpython.com/python-f-strings/
As of Python 3.6, f-strings are a great new way to format strings. Not only are they more readable, more concise, and less prone to error than other ways of formatting, …
_________
""" 
# Your code should go here:

def hello(name1):
    return ("Hello {}!".format(name1))

print(hello("Nitkarsh"))
print(hello("Anmol"))
print(hello("Rohit"))
print(hello("Santosh"))
print(hello("Varsha"))

# The program is complete.