"""
##Barbecue Skewers

You are in charge of the barbecue grill. A vegetarian skewer is a skewer that has only vegetables (-o). A non-vegetarian skewer is a skewer with at least one piece of meat (-x).
For example, the grill below has 4 non-vegetarian skewers and 1 vegetarian skewer (the one in the middle).
___
["--xo--x--ox--",
"--xx--x--xx--",
"--oo--o--oo--",      <<< vegetarian skewer
"--xx--x--ox--",
"--xx--x--ox--"]
_____

Given a BBQ grill, write a function that returns [# vegetarian skewers, # non-vegetarian skewers]. For example above, the function should return [1, 4].


[Examples]

___
bbq_skewers([
  "--oooo-ooo--",
  "--xx--x--xx--",
  "--o---o--oo--",
  "--xx--x--ox--",
  "--xx--x--ox--"
]) ➞ [2, 3]

bbq_skewers([
  "--oooo-ooo--",
  "--xxxxxxxx--",
  "--o---",
  "-o-----o---x--",
  "--o---o-----"
]) ➞ [3, 2]
_____



[Notes]

N/A


[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to check if a Python string contains another string?
https://www.afternerd.com/blog/python-string-contains/
One of the most common operations that programmers use on strings is to check whether a string contains some other string. If you are coming to Python from Java, you mi …
_________
_________
How to check a string for specific characters?
https://stackoverflow.com/questions/5188792/how-to-check-a-string-for-specific-characters
How can I check if a string value has exact characters in it using Python2? Specifically, I am looking to detect if it has dollar signs ("$"), commas (","), and numbers.
_________
_________
Find Size of a List in Python
https://www.geeksforgeeks.org/find-size-of-a-ist-in-python/
Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a diction …
_________
""" 
# Your code should go here:

