"""
####  Hall Monitor  ####

A floor plan is arranged as follows:
___
*) Four rooms, which all lead into the hallway.
*) It's impossible to move between rooms without first going into the hallway.
___


Create a function that validates whether the path between rooms is possible. The hallway will be given as the letter "H".


[Examples]

___
possible_path([1, "H", 2, "H", 3, "H", 4]) ➞ True

possible_path(["H", 3, "H"]) ➞ True

possible_path([1, 2, "H", 3]) ➞ False
_____



[Notes]

___
*) A route may begin or end in a hallway.
*) All inputs are either numbers 1-4, or the letter "H".
*) No rooms will repeat.
___



[algorithms] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Separate Odd and Even Index Elements
https://www.geeksforgeeks.org/python-separate-odd-and-even-index-elements/
Python list are quite popular and no matter what type of field one is coding, one has to deal with lists and its various applications. In this particular article, we di …
_________
_________
all() Method
https://www.w3schools.com/python/ref_func_all.asp
Returns True if all items in an iterable are true, otherwise it returns False.
_________
_________
zip() Method
https://www.w3schools.com/python/ref_func_zip.asp
Returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator a …
_________

"""
#Your code should go here:

