"""
##Clear the Fog

Create a function which returns the word in the string, but with all the fog letters removed. However, if the string is clear from fog, return "It's a clear day!".


[Examples]

___
clear_fog("sky") ➞ "It's a clear day!"

clear_fog("fogfogFFfoooofftogffreogffesGgfOogfog") ➞ "trees"

clear_fog("fogFogFogffoObirdsanffodthebffoeffoesGGGfOgFog") ➞ "birdsandthebees"
_____



[Notes]

___
*) Hidden words won't include the letters f, o or g.
*) Hidden words are always in lowercase.
___



[formatting] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
strip() Method
https://www.w3schools.com/python/ref_string_strip.asp
Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove).
_________
_________
How to remove specific characters from a string in Python?
https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
I'm trying to remove specific characters from a string using Python. This is the code I'm using right now. Unfortunately it appears to do nothing to the string. How do …
_________
_________
filter() Method
https://thepythonguru.com/python-builtin-functions/filter/
Apply a function on all the elements of an iterable and discard those evaluated as False. It generates a lazy iterator for which it is necessary to use type conversion …
_________
""" 
# Your code should go here:

