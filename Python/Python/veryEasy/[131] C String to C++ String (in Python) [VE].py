"""
##C String to C++ String (in Python)

This is a list of single characters with an unwanted character at the end:
___
["H", "e", "l", "l", "o", "!", "\0"]
_____

You could also just type "Hello!" when initializing a variable, creating the string "Hello!"
Create a function that will return a string by combining the given character list, not including the unwanted final character.


[Examples]

___
cpp_txt(["H", "i", "!", "\0"]) ➞ "Hi!"

cpp_txt(["H", "e", "l", "l", "o", "!", "\0"]) ➞ "Hello!"

cpp_txt(["J", "A", "V", "a", "\0"]) ➞ "JAVa"
_____



[Notes]

This is a translation of a C++ challenge and is trivial in Python, but perhaps it will be helpful to someone out there. (No challenge is trivial until you know how to solve it :)


[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
join() Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable.
_________
_________
remove() Method
https://www.programiz.com/python-programming/methods/list/remove
Removes the first matching element (which is passed as an argument) from the list.
_________
_________
pop() Method
https://www.programiz.com/python-programming/methods/list/pop
Removes the item at the given index from the list and returns the removed item.
_________
_________
Remove Final Character From A String
https://stackoverflow.com/questions/15478127/remove-final-character-from-string
If my string is "abcdefghij" (I do not want to replace the 'j' character, since my string may contain multiple 'j' characters) I only want the last character gone. Rega …
_________
""" 
# Your code should go here:

