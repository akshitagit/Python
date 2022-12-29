"""
##Total Volume of All Boxes

Given a list of boxes, create a function that returns the total volume of all those boxes combined together. A box is represented by a list with three elements: length, width and height.
For instance, total_volume([2, 3, 2], [6, 6, 7], [1, 2, 1]) should return 266 since (2 x 3 x 2) + (6 x 6 x 7) + (1 x 2 x 1) = 12 + 252 + 2 = 266.


[Examples]

___
total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]) ➞ 63

total_volume([2, 2, 2], [2, 1, 1]) ➞ 10

total_volume([1, 1, 1]) ➞ 1
_____



[Notes]

___
*) You will be given at least one box.
*) Each box will always have three dimensions included.
___



[arrays] [geometry] [math] 



-------------------------------------------------------------------
[Resources]
_________
Returning the product of a list?
https://stackoverflow.com/questions/2104782/returning-the-product-of-a-list
Is there a more concise, efficient or simply pythonic way to do the following?
_________
_________
*args and **kwargs in Python
https://www.geeksforgeeks.org/args-kwargs-python/
The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-le …
_________
_________
Reduce Function
http://book.pythontips.com/en/latest/map_filter.html#reduce
Reduce is a really useful function for performing some computation on a list and returning the result. It applies a rolling computation to sequential pairs of values in …
_________
_________
numpy.prod()
https://docs.scipy.org/doc/numpy/reference/generated/numpy.prod.html
Return the product of array elements over a given axis.
_________
_________
*args and **kwargs in Python explained
https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
I have come to see that most new python programmers have a hard time figuring out the *args and **kwargs magic variables. So what are they ? First of all let me tell yo …
_________
""" 
# Your code should go here:

