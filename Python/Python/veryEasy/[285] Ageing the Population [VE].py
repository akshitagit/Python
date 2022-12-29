"""
##Ageing the Population...

Given a dictionary of people and their ages, return how old the people would be after n years have passed. Use the absolute value of n.


[Examples]

___
after_n_years({
  "Joel" : 32,
  "Fred" : 44,
  "Reginald" : 65,
  "Susan" : 33,
  "Julian" : 13
}, 1) ➞ {
  "Joel" : 33,
  "Fred" : 45,
  "Reginald" : 66,
  "Susan" : 34,
  "Julian" : 14
}

after_n_years({
  "Baby" : 2,
  "Child" : 8,
  "Teenager" : 15,
  "Adult" : 25,
  "Elderly" : 71
}, 19) ➞ {
  "Baby" : 21,
  "Child" : 27,
  "Teenager" : 34,
  "Adult" : 44,
  "Elderly" : 90
}

after_n_years({
  "Genie" : 1000,
  "Joe" : 40
}, 5) ➞ {
  "Genie" : 1005,
  "Joe" : 45
}
_____



[Notes]

___
*) Assume that everyone is immortal (it would be a bit grim if I told you to remove names once they reached 75).
*) n should be a positive number because last time I checked, people don't tend to age backwards. Therefore, use the absolute value of n.
___



[arrays] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
items() Method
https://www.programiz.com/python-programming/methods/dictionary/items
Returns a view object that displays a list of dictionary's (key, value) tuple pairs.
_________
_________
How to Iterate Through a Dictionary in Python
https://realpython.com/iterate-through-dictionary-python/#how-to-iterate-through-a-dictionary-in-python-the-basics
Dictionaries are a useful and widely used data structure in Python. As a Python coder, you’ll often be in situations where you’ll need to iterate through a dictionary i …
_________
_________
Replace All Values in a Dictionary
https://stackoverflow.com/questions/12960907/python-replace-all-values-in-a-dictionary
Iterate through a dictionary and return a new one by changing its values or keys.
_________
_________
Python Basic: Exercises, Practice, Solution
https://www.w3resource.com/python-exercises/python-basic-exercises.php
Write a Python program to print the following string in a specific format (see the output). Go to the editor. Sample String : "Twinkle, twinkle, little star, How I wo …
_________
_________
Python Dictionary Comprehension
https://www.programiz.com/python-programming/dictionary-comprehension
In this tutorial, we will learn about Python dictionary comprehension and how to use it with the help of examples. Dictionaries are data types in Python which allows us …
_________
_________
keys() Method
https://www.geeksforgeeks.org/python-dictionary-keys-method/
Returns a view object that displays a list of all the keys in the dictionary.
_________
_________
update() Method
https://www.programiz.com/python-programming/methods/dictionary/update
Updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.
_________
""" 
# Your code should go here:

