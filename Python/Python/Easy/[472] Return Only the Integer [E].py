"""
##Return Only the Integer

Write a function that takes a list of elements and returns only the integers.


[Examples]

___
return_only_integer([9, 2, "space", "car", "lion", 16]) ➞ [9, 2, 16]

return_only_integer(["hello", 81, "basketball", 123, "fox"]) ➞ [81, 123]

return_only_integer([10, "121", 56, 20, "car", 3, "lion"]) ➞ [10, 56, 20, 3]

return_only_integer(["String",  True,  3.3,  1]) ➞ [1]
_____



[Notes]

N/A


[arrays] [language_fundamentals] [loops] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
class type(object)
https://docs.python.org/3/library/functions.html#type
With one argument, return the type of an object. The return value is a type object and generally the same object as returned by object.__class__. The isinstance() buil …
_________
_________
What are the differences between type() and isinstance()?
https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance
To summarize the contents of other (already good!) answers, isinstance caters for inheritance (an instance of a derived class is an instance of a base class, too), whil …
_________
_________
Checking whether a variable is an integer or not?
https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not
If you need to do this, do isinstance(<var>, int) unless you are in Python 2.x in which case you want isinstance(<var>, (int, long)) Do not use type. It is almost never …
_________
_________
Extract Numbers From String
https://www.geeksforgeeks.org/python-extract-numbers-from-string/?ref=lbp
Many times, while working with strings we come across this issue in which we need to get all the numeric occurrences. This type of problem generally occurs in competiti …
_________
_________
Extract Integers From Mixed List
https://stackoverflow.com/questions/26725535/python-extract-integers-from-mixed-list
How to extract integers from a mixed list in Python.
_________
""" 
# Your code should go here:

