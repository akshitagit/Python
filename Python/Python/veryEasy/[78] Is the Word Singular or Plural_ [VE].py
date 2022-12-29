"""
##Is the Word Singular or Plural?

Create a function that takes in a word and determines whether or not it is plural. A plural word is one that ends in "s".


[Examples]

___
is_plural("changes") ➞ True

is_plural("change") ➞ False

is_plural("dudes") ➞ True

is_plural("magic") ➞ False
_____



[Notes]

___
*) Don't forget to return the result.
*) Remember that return True (boolean) is not the same as return "True" (string).
*) This is an oversimplification of the English language. We are ignoring edge cases like "goose" and "geese", "fungus" and "fungi", etc.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[conditions] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
endswith() Method
https://www.programiz.com/python-programming/methods/string/endswith
Returns True if a string ends with the specified suffix. If not, it returns False.
_________
_________
All Built-in Functions
https://www.w3schools.com/python/python_ref_functions.asp
Python has a set of built-in functions. This is a full list of all.
_________
_________
How to get Last N characters in a string?
https://thispointer.com/python-how-to-get-last-n-characters-in-a-string/
How to get Last N characters in a string?
_________
_________
Python Strings
https://developers.google.com/edu/python/strings
Python has a built-in string class named "str" with many handy features (there is an older module named "string" which you should not use). String literals can be enclo …
_________
""" 
# Your code should go here:

isPlural = lambda str1 : True if str1[-1].lower() == "s" else False

print(isPlural("Nitkarsh"))
print(isPlural("strings"))
print(isPlural("S"))
print(isPlural("sayS"))

# The program is complete.