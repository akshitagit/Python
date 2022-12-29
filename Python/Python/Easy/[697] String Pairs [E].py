"""
####  String Pairs  ####

Create a function that takes a string s and returns a list of two-paired characters. If the string has an odd number of characters, add an asterisk * in the final pair.
See the below examples for a better understanding:


[Examples]

___
string_pairs("mubashir") ➞ ["mu", "ba", "sh", "ir"]

string_pairs("edabit") ➞ ["ed", "ab", "it"]

string_pairs("airforces") ➞ ["ai", "rf", "or", "ce", "s*"]
_____



[Notes]

Return [] if the given string is empty.


[arrays] [conditions] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
re.match(), re.search(), re.findall()
https://www.guru99.com/python-regular-expressions-complete-tutorial.html
A Regular Expression (RE) in a programming language is a special text string used for describing a search pattern. It is extremely useful for extracting information fro …
_________
_________
len() Method
https://www.geeksforgeeks.org/python-string-length-len/
Returns the length of the string.
_________
_________
zip() Function
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and return it. In this tutorial, we will learn about Python zip() in detail with the help of examples.
_________
_________
How to Combine Pairs of Strings in a List in Python
https://www.kite.com/python/answers/how-to-combine-pairs-of-strings-in-a-list-in-python
Given a list of strings, such as ['a', 'b', 'c', 'd'], combining each pair would result in ["ab", "cd"]. Use the syntax [list[i] + list[i+1] for i in range(0, len(list) …
_________
_________
Split String Into a List, With Items of Equal Length
https://stackoverflow.com/questions/22656768/split-string-into-a-list-with-items-of-equal-length
I have a string (without spaces) which I need to split into a list with items of equal length. I'm aware of the split() method, but as far as I'm aware this only splits …
_________

"""
#Your code should go here:

