"""
####  List Chunking  ####

Given a list and chunk size "n", create a function such that it divides the list into many sublists where each sublist is of length size "n".


[Examples]

___
chunk([1, 2, 3, 4], 2) ➞ [
  [1, 2], [3, 4]
]

chunk([1, 2, 3, 4, 5, 6, 7], 3) ➞ [
  [1, 2, 3], [4, 5, 6], [7]
]

chunk([1, 2, 3, 4 ,5], 10) ➞ [
  [1, 2, 3, 4, 5]
]
_____



[Notes]

Remember that number of sublists may not be equal to chunk size.


[arrays] [conditions] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Extended Slices
https://docs.python.org/2.3/whatsnew/section-slices.html
Ever since Python 1.4, the slicing syntax has supported an optional third ``step'' or ``stride'' argument. For example, these are all legal Python syntax: L[1:10:2], L[ …
_________
_________
Data Structures
https://docs.python.org/3/tutorial/datastructures.html
This chapter describes some things you’ve learned about already in more detail, and adds some new things as well.
_________
_________
How do you split a list into evenly sized chunks?
https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
You can simply use list comprehension instead of writing a function, though it's a good idea to encapsulate operations like this in named functions so that your code is …
_________

"""
#Your code should go here:

