"""
##Return Sole Element in a Set

Given a set containing one element, return the element.


[Examples]

___
element_from_set({"edabit"}) ➞ "edabit"

element_from_set({True}) ➞ True

element_from_set({11037}) ➞ 11037
_____



[Notes]

Lists, dictionaries, and other sets won't be elements because sets won't accept any mutable data types as elements.


[language_fundamentals] [objects] 



-------------------------------------------------------------------
[Resources]
_________
pop() Method
https://www.programiz.com/python-programming/methods/list/pop
Removes the item at the given index from the list and returns the removed item.
_________
_________
How to access the sole element of a set?
https://stackoverflow.com/questions/20625579/access-the-sole-element-of-a-set
I have a set in Python from which I am removing elements one by one based on a condition. When the set is left with just 1 element, I need to return that element. How d …
_________
_________
max() and min() in Python
https://www.geeksforgeeks.org/max-min-python/
Those two work as well if you don't want to remove the sole element from set.
_________
_________
Sets
https://realpython.com/python-sets/
Grouping objects into a set can be useful in programming as well, and Python provides a built-in set type to do so. Sets are distinguished from other object types by th …
_________
""" 
# Your code should go here:

def minFunc(set1):
    return min(set1)
def maxFunc(set1):
    return max(set1)
def popFunc(set1):
    return set1.pop()

def listFunc(set1):
    return list(set1)[0]

print("minFunc is being used here.")
print(minFunc({"Nitkarsh"}))
print(minFunc({True}))
print(minFunc({11037}))

print("\nmaxFunc is being used here.")
print(maxFunc({"Nitkarsh"}))
print(maxFunc({True}))
print(maxFunc({11037}))

print("\npopFunc is being used here.")
print(popFunc({"Nitkarsh"}))
print(popFunc({True}))
print(popFunc({11037}))

print("\nlistFunc is being used here.")
print(listFunc({"Nitkarsh"}))
print(listFunc({True}))
print(listFunc({11037}))

# The program is complete.