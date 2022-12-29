"""
##Convert Key, Values in a Dictionary to List

Write a function that converts a dictionary into a list of keys-values tuples.


[Examples]

___
dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]

dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
_____



[Notes]

Return the elements in the list in alphabetical order.


[arrays] [objects] 



-------------------------------------------------------------------
[Resources]
_________
items() Method
https://www.programiz.com/python-programming/methods/dictionary/items
Returns a view object that displays a list of dictionary's (key, value) tuple pairs.
_________
_________
sorted() Method
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable.
_________
_________
How can I convert a dictionary into a list of tuples?
https://stackoverflow.com/questions/674519/how-can-i-convert-a-dictionary-into-a-list-of-tuples
If I have a dictionary like: { 'a': 1, 'b': 2, 'c': 3 } How can I convert it to this? [ ('a', 1), ('b', 2), ('c', 3) ] And how can I convert it to this? [ (1, 'a'), …
_________
_________
zip() Method
https://www.w3schools.com/python/ref_func_zip.asp
Returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator a …
_________
_________
Itemgetter
https://riptutorial.com/python/example/923/itemgetter
Grouping the key-value pairs of a dictionary by the value with Itemgetter.
_________
""" 
# Your code should go here:

