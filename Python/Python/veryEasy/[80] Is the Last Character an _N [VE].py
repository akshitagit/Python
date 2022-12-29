"""
##Is the Last Character an "N"?

Create a function that takes a string (a random name). If the last character of the name is an "n", return True, otherwise return False.


[Examples]

___
is_last_character_n("Aiden") ➞ True

is_last_character_n("Piet") ➞ False

is_last_character_n("Bert") ➞ False

is_last_character_n("Dean") ➞ True
_____



[Notes]

The function must return a boolean value ( i.e. True or False).


[conditions] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
endswith() Method
https://www.programiz.com/python-programming/methods/string/endswith
Returns True if a string ends with the specified suffix. If not, it returns False.
_________
_________
How to check a string's first and last letters?
https://stackoverflow.com/questions/19954593/python-checking-a-strings-first-and-last-character
When you say [:-1] you are stripping the last element. Instead of slicing the string, you can apply startswith and endswith on the string object itself like this: if st …
_________
_________
Online Regex Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
""" 
# Your code should go here:

nLastIs = lambda rName1 : True if rName1[-1].lower() == "n" else False

print(nLastIs("Nitkarsh"))
print(nLastIs("n"))
print(nLastIs("N"))
print(nLastIs("Dean"))

# The program is complete.