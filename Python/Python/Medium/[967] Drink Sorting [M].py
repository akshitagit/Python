"""
####  Drink Sorting  ####

You will be given a list of drinks, with each drink being a dictionary with two properties: name and price. Create a function that has the drinks list as an argument and return the drinks dictionaries sorted by price in ascending order.
Assume that the following array of drink objects needs to be sorted:
___
drinks = [
  {"name": "lemonade", "price": 50},
  {"name": "lime", "price": 10}
]
_____

The output of the sorted drinks object will be:


[Examples]

___
sort_drinks_by_price(drinks) ➞ [{name: "lime", price: 10}, {name: "lemonade", price: 50}]
_____



[Notes]

N/A


[objects] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
Ways to Sort List of Dictionaries by Values in Python
https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-itemgetter/
Itemgetter can be used instead of lambda function to achieve the similar functionality. Outputs in same way as sorted() and lambda, but has different internal implement …
_________
_________
sorted()
https://stackoverflow.com/questions/45936929/python-sorted-with-lambda
Sorts the elements of a given iterable in a specific order (either ascending or descending) and returns the sorted iterable as a list. sorted(iterable, key=None, revers …
_________

"""
#Your code should go here:

