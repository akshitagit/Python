"""
##Burglary Series (14): Adjectives Total

You call your spouse in anger and a "little" argument takes place. Count the total amount of insults used. Given a dictionary of insults, return the total amount of insults used.


[Examples]

___
total_amount_adjectives({ "a": "moron" }) ➞ 1

total_amount_adjectives({ "a": "idiot", "b": "idiot", "c": "idiot" }) ➞ 3

total_amount_adjectives({ "a": "moron", "b": "scumbag", "c": "moron", d: "dirtbag" }) ➞ 4
_____



[Notes]

The dictionary will never be empty.


[arrays] [language_fundamentals] [objects] 



-------------------------------------------------------------------
[Resources]
_________
len() Function
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
_________
Count Number of Keys in Dictionary
https://www.delftstack.com/howto/python/number-of-keys-in-dictionary-python/#:~:text=the%20same%20purpose.-,Use%20the%20len()%20Function%20to%20Count%20the%20Number%20of,total%20number%20using%20len()%20.
This tutorial demonstrates how to count the number of keys in a Python dictionary.
_________
_________
Get Number of Elements
https://stackabuse.com/python-get-number-of-elements-in-a-list/
Getting the number of elements in a list in Python is a common operation. For example, you will need to know how many elements the list has whenever you iterate through …
_________
_________
Number of Keys in an Object
https://www.delftstack.com/howto/python/number-of-keys-in-dictionary-python/#:~:text=the%20same%20purpose.-,Use%20the%20len()%20Function%20to%20Count%20the%20Number%20of,total%20number%20using%20len()%20.
We will discuss how to count the number of keys in a Python dictionary using the len() function and also create our own function for the same purpose.
_________
""" 
# Your code should go here:

def countKeys(dict):
    count = 0
    for i in enumerate(dict):
        count += 1
    if count <= 0:
        return "Input dictionary cannot be zero!"
    else:
        return ("Total amount of insults used: {}".format(count))


print(countKeys({ "a": "moron" }))
print(countKeys({ "a": "idiot", "b": "idiot", "c": "idiot" }))
print(countKeys({ "a": "moron", "b": "scumbag", "c": "moron", "d": "dirtbag" }))
print(countKeys({}))

# The program is complete.