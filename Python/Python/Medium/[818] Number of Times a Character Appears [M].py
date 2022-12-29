"""
####  Number of Times a Character Appears  ####

Create a function that returns the number of times a character appears in each word in a sentence. Treat upper and lower case characters of the same letter as being identical (e.g. a exists in Anna twice, not once).


[Examples]

___
char_appears("She sells sea shells by the seashore.", "s")
➞ [1, 2, 1, 2, 0, 0, 2]
# "s" shows up once in "She", twice in "sells", once in "sea", twice in "shells", etc.

char_appears("Peter Piper picked a peck of pickled peppers.", "P")
➞ [1, 2, 1, 0, 1, 0, 1, 3]
# "p" shows up once in "Peter", ... 3 times in "peppers".

char_appears("She hiked in the morning, then swam in the river.", "t")
➞ [0, 0, 0, 1, 0, 1, 0, 0, 1, 0]
_____



[Notes]

Ignore case (note that capitalization, in both the sentence and character itself, in examples #1 & #2).


[arrays] [strings] 



-------------------------------------------------------------------
[Resources]
_________
count() Method
https://docs.python.org/2/library/string.html#string.count
Return the number of (non-overlapping) occurrences of substring sub in string s[start:end]. Defaults for start and end and interpretation of negative values are the sam …
_________
_________
When to Use a List Comprehension
https://realpython.com/list-comprehension-python/
Understand the full power of Python list comprehensions and how to use their features comfortably. Gain an understanding of the trade-offs that come with using them so …
_________
_________
split() Method
https://www.geeksforgeeks.org/python-string-split/
Returns a list of strings after breaking the given string by the specified separator.
_________

"""
#Your code should go here:

