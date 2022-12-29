"""
####  Filtering by Star Rating  ####

Given a dictionary of some items with star ratings and a specified star rating, return a new dictionary of items which match the specified star rating. Return "No results found" if no item matches the star rating given.


[Examples]

___
filter_by_rating({
  "Luxury Chocolates" : "*****",
  "Tasty Chocolates" : "****",
  "Aunty May Chocolates" : "*****",
  "Generic Chocolates" : "***"
}, "*****") ➞ {
  "Luxury Chocolates" : "*****",
  "Aunty May Chocolates" : "*****"
}

filter_by_rating({
  "Continental Hotel" : "****",
  "Big Street Hotel" : "**",
  "Corner Hotel" : "**",
  "Trashviews Hotel" : "*",
  "Hazbins" : "*****"
}, "*") ➞ {
  "Trashviews Hotel" : "*"
}

filter_by_rating({
  "Solo Restaurant" : "***",
  "Finest Dinings" : "*****",
  "Burger Stand" : "***"
}, "****") ➞ "No results found"
_____



[Notes]

N/A


[arrays] [data_structures] [objects] 



-------------------------------------------------------------------
[Resources]
_________
How to Filter a Dictionary in Python?
https://blog.finxter.com/how-to-filter-a-dictionary-in-python/
Problem: Given a dictionary and a filter condition. How to filter a dictionary by … … key so that only those (key, value) pairs in the dictionary remain where the key …
_________
_________
Best Way to Filter a Dictionary
https://stackoverflow.com/questions/8425046/the-best-way-to-filter-a-dictionary-in-python
Best way to filter a dictionary in Python.
_________
_________
How to add a key:value pair to a dictionary?
https://www.geeksforgeeks.org/add-a-keyvalue-pair-to-dictionary-in-python/
Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an el …
_________
_________
Get Key by Value in Dictionary
https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
I made a function which will look up ages in a Dictionary and show the matching name. I know how to compare and find the age I just don't know how to show the name of t …
_________

"""
#Your code should go here:

