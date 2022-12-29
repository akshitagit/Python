"""
####  International Greetings  ####

Suppose you have a guest list of students and the country they are from, stored as key-value pairs in a dictionary.
___
GUEST_LIST = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}
_____

Write a function that takes in a name and returns a name tag, that should read:
___
"Hi! I'm [name], and I'm from [country]."
_____

If the name is not in the dictionary, return:
___
"Hi! I'm a guest."
_____



[Examples]

___
greeting("Randy") ➞ "Hi! I'm Randy, and I'm from Germany."

greeting("Sam") ➞ "Hi! I'm Sam, and I'm from Argentina."

greeting("Monti") ➞ "Hi! I'm a guest."
_____



[Notes]

N/A


[formatting] [objects] 



-------------------------------------------------------------------
[Resources]
_________
How To Use String Formatters in Python
https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
Allows you to do variable substitutions and value formatting. This lets you concatenate elements together within a string through positional formatting.
_________
_________
get() Method
https://www.tutorialspoint.com/python/dictionary_get.htm
Returns a value for the given key. If key is not available then returns default value None.
_________
_________
f-Strings: An Improved String Formatting Syntax (Guide)
https://realpython.com/python-f-strings/
As of Python 3.6, f-strings are a great new way to format strings. Not only are they more readable, more concise, and less prone to error than other ways of formatting, …
_________
_________
How to do a dictionary format with f-string in Python 3.6?
https://stackoverflow.com/questions/43488137/how-to-do-a-dictionary-format-with-f-string-in-python-3-6
Depending on the number of contributions your dictionary makes to a given string you might consider using .format(**dict) instead to make it more readable, even though …
_________

"""
#Your code should go here:

