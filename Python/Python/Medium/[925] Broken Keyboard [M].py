"""
####  Broken Keyboard  ####

Given what is supposed to be typed and what is actually typed, write a function that returns the broken key(s). The function looks like:
___
find_broken_keys(correct phrase, what you actually typed)
_____



[Examples]

___
find_broken_keys("happy birthday", "hawwy birthday") ➞ ["p"]

find_broken_keys("starry night", "starrq light") ➞ ["y", "n"]

find_broken_keys("beethoven", "affthoif5") ➞ ["b", "e", "v", "n"]
_____



[Notes]

___
*) Broken keys should be ordered by when they first appear in the sentence.
*) Only one broken key per letter should be listed.
*) Letters will all be in lower case.
___



[arrays] [strings] 



-------------------------------------------------------------------
[Resources]
_________
OrderedDict
https://pymotw.com/3/collections/ordereddict.html
Is a dictionary subclass that remembers the order in which its contents are added. Remember the Order Keys are Added to a Dictionary.
_________
_________
set() Method
https://www.geeksforgeeks.org/python-set-method/
Used to convert any of the iterable to the distinct element and sorted sequence of iterable elements, commonly called Set.
_________

"""
#Your code should go here:

