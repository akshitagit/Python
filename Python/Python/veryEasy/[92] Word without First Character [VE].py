"""
##Word without First Character

Create a function that takes a word and returns the new word without including the first character.


[Examples]

___
new_word("apple") ➞ "pple"

new_word("cherry") ➞ "herry"

new_word("plum") ➞ "lum"
_____



[Notes]

The input is always a valid word.


[formatting] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Ways to Remove i'th Character from String in Python
https://www.geeksforgeeks.org/ways-to-remove-ith-character-from-string-in-python/
Presents one such problem of removing i’th character from string and talks about possible solutions that can be employed in achieving them.
_________
_________
Accessing Values in Strings
https://www.tutorialspoint.com/python/python_strings.htm
To access substrings, use the square brackets for slicing along with the index or indices
_________
_________
Python3 Cheatsheet
https://programmingwithmosh.com/wp-content/uploads/2019/02/Python-Cheat-Sheet.pdf
Find the subheading STRINGS and read to find information on string manipulation.
_________
_________
How to Substring a String
https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
It follows this template: string[start: end: step] start: The starting index of the substring. The character at this index is included in the substring. If start is not …
_________
_________
Python Remove Character from String
https://www.journaldev.com/23674/python-remove-character-from-string
Sometimes we want to remove all occurrences of a character from a string. There are two common ways to achieve this: using string replace() function or using string tra …
_________
_________
remove() Method
https://www.programiz.com/python-programming/methods/list/remove
Removes the first matching element (which is passed as an argument) from the list.
_________
""" 
# Your code should go here:

removeFirst = lambda word : word[1:] if len(word) > 0  else "Please input a valid word."

print(removeFirst("Nitkarsh"))
print(removeFirst("Anmol"))
print(removeFirst("Rohit"))
print(removeFirst("Purshotam"))

# The program is complete.