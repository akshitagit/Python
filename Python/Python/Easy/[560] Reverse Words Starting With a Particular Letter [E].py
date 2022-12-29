"""
##Reverse Words Starting With a Particular Letter

Write a function that reverses all the words in a sentence that start with a particular letter.


[Examples]

___
special_reverse("word searches are super fun", "s")
➞ "word sehcraes are repus fun"

special_reverse("first man to walk on the moon", "m")
➞ "first nam to walk on the noom"

special_reverse("peter piper picked pickled peppers", "p")
➞ "retep repip dekcip delkcip sreppep"
_____



[Notes]

___
*) Reverse the words themselves, not the entire sentence.
*) All characters in the sentence will be in lower case.
___



[higher_order_functions] [strings] 



-------------------------------------------------------------------
[Resources]
_________
join() Method
https://www.w3schools.com/python/ref_string_join.asp
Takes all items in an iterable and joins them into one string.
_________
_________
startswith() Method
https://www.tutorialspoint.com/python/string_startswith.htm
Checks whether string starts with str, optionally restricting the matching with the given indices start and end.
_________
_________
How to Reverse a String in Python
https://www.w3schools.com/python/python_howto_reverse_string.asp
There is no built-in function to reverse a String in Python. The fastest (and easiest?) way is to use a slice that steps backwards, -1.
_________
_________
if/else in Python list comprehension?
https://stackoverflow.com/questions/4260280/if-else-in-pythons-list-comprehension
How can I do the following? row = [unicode(x.strip()) for x in row if x is not None else ''] Essentially: 1. Replace all the Nones with empty strings, and then ... 2. C …
_________
_________
split( ) Method
https://www.programiz.com/python-programming/methods/string/split
Breaks up a string at the specified separator and returns a list of strings.
_________
_________
List Comprehension
https://www.programiz.com/python-programming/list-comprehension
An elegant way to define and create lists based on existing lists.
_________
""" 
# Your code should go here:

