"""
##Check if objOne Is Equal to objTwo

Create a function that checks to see if two object arguments are equal to one another. Return True if the objects are equal, otherwise, return False.


[Examples]

___
# The first object parameter.

obj_one = {
  "name": "Benny",
  "phone": "3325558745",
  "email": "benny@edabit.com"
}

# The second object parameter.

obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}


is_equal(obj_one, obj_two)
➞ False
_____

___
# The first object parameter.

obj_one = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}

# The second object parameter.

obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}


is_equal(obj_one, obj_two)
➞ True
_____



[Notes]

If you have a suggestion on how to make these instructions easier to understand, please leave a comment. Your feedback is greatly appreciated.


[language_fundamentals] [objects] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Compare Dictionaries
https://www.kite.com/python/answers/how-to-compare-dictionaries-in-python
Checks each corresponding key-value pair between the two dictionaries for equality. For example, both {"a": 1, "b": 2} and {"b": 2, "c": 3} have the key-value pair {"b" …
_________
_________
Comparing Objects
https://realpython.com/python-is-identity-vs-equality/
The == operator compares the value or equality of two objects, whereas the Python is operator checks whether two variables point to the same object in memory. In the va …
_________
""" 
# Your code should go here:

def isEqual(obj1, obj2):
    if obj1 == obj2:
        return True
    else:
        return False

# Direct printing method works.
print(isEqual({
  "name": "Benny",
  "phone": "3325558745",
  "email": "benny@edabit.com"
},{
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}))

# Assigning and then using as a parameter works.
obj1 = { 
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}
obj2 = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}

print(isEqual(obj1, obj2))

# The program is complete.