"""
####  Total Sales of Product  ####

In this question you will be given a table as below, where the first row lists the names of products, and each of row after that lists the sales of the product for each day (over some time range).
___
[
  ["A", "B", "C"],
  [ 2 ,  7 ,  1 ],
  [ 3 ,  6 ,  6 ],
  [ 4 ,  5 ,  5 ]
]
_____

Write a function that receives:
___
*) A sales table sales_table as shown above.
*) The name of a product product.
___

... and returns the total sales if the product is on the list, otherwise return the string "Product not found".


[Examples]

___
total_sales([
  ["A", "B", "C"],
  [ 2 ,  7 ,  1 ],
  [ 3 ,  6 ,  6 ],
  [ 4 ,  5 ,  5 ]
], "A") ➞ 9

# 2 + 3 + 4 = 9


total_sales([
  ["A", "B", "C"],
  [ 2 ,  7 ,  1 ],
  [ 3 ,  6 ,  6 ],
  [ 4 ,  5 ,  5 ]
], "C") ➞ 12

# 1 + 6 + 5 = 12


total_sales([
  ["A", "B", "C"],
  [ 2 ,  7 ,  1 ],
  [ 3 ,  6 ,  6 ],
  [ 4 ,  5 ,  5 ]
], "D") ➞ "Product not found"
_____



[Notes]

The examples above all use the same sales table, but in the tests the table will vary.


[arrays] [data_structures] [language_fundamentals] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Using the zip() Function in Python
https://realpython.com/python-zip-function/
Python’s zip() function creates an iterator that will aggregate elements from two or more iterables. You can use the resulting iterator to quickly and consistently solv …
_________
_________
index() Method
https://www.programiz.com/python-programming/methods/list/index
Searches an element in the list and returns its index.
_________
_________
Find Indices of a Value in 2d Matrix
https://stackoverflow.com/questions/17385419/find-indices-of-a-value-in-2d-matrix/17388914
If you want all of the locations that the value appears at, you can use the following list comprehension with val set to whatever you're searching for...
_________
_________
How to Zip Lists in a List
https://stackoverflow.com/questions/4112265/how-to-zip-lists-in-a-list
The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments. For …
_________

"""
#Your code should go here:

