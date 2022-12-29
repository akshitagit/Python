"""
####  Finding Nemo  ####

You're given a string of words. You need to find the word "Nemo", and return a string like this: "I found Nemo at [the order of the word you find Nemo]!".
If you can't find Nemo, return "I can't find Nemo :(".


[Examples]

___
find_nemo("I am finding Nemo !") ➞ "I found Nemo at 4!"

find_nemo("Nemo is me") ➞ "I found Nemo at 1!"

find_nemo("I Nemo am") ➞ "I found Nemo at 2!"
_____



[Notes]

___
*) ! , ? . are always separated from the last word.
*) Nemo will always look like Nemo, and not NeMo or other capital variations.
*) Nemo's, or anything that says Nemo with something behind it, doesn't count as Finding Nemo.
*) If there are multiple Nemo's in the sentence, only return the first one.
___



[arrays] [formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Is there a short contains function for lists?
https://stackoverflow.com/questions/12934190/is-there-a-short-contains-function-for-lists
I see people are using any to gather another list to see if an item exists in a list, but is there a quick way to just do?: if list.contains(myItem): # do something
_________
_________
index() Method
https://www.programiz.com/python-programming/methods/list/index
Searches an element in the list and returns its index.
_________
_________
find() Method
https://www.geeksforgeeks.org/string-find-python/
Returns the lowest index of the substring if it is found in given string. If its is not found then it returns -1.
_________
_________
split() Method
https://www.programiz.com/python-programming/methods/string/split
Breaks up a string at the specified separator and returns a list of strings.
_________
_________
Type Conversion in Python
https://www.geeksforgeeks.org/type-conversion-python/
Python defines type conversion functions to directly convert one data type to another which is useful in day to day and competitive programming. This article is aimed a …
_________

"""
#Your code should go here:

