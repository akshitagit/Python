"""
##Return the Last Element in a List

Create a function that accepts a list and returns the last item in the list. The list can be either homogeneous or heterogeneous.


[Examples]

___
get_last_item([1, 2, 3]) ➞ 3

get_last_item(["cat", "dog", "duck"]) ➞ "duck"

get_last_item([True, False, True]) ➞ True

get_last_item([7, "String", False]) ➞ False
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[arrays] [language_fundamentals] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Getting the Last Element of a List in Python
http://stackoverflow.com/questions/930397/getting-the-last-element-of-a-list-in-python
some_list[-1] is the shortest and most Pythonic. In fact, you can do much more with this syntax. The some_list[-n] syntax gets the nth-to-last element. So some_list[-1] …
_________
_________
pop() Method
https://www.programiz.com/python-programming/methods/list/pop
Removes and returns the element at the given index (passed as an argument) from the list. The syntax of pop() method is: list.pop(index)
_________
_________
How to get the last element of a list in Python?
https://www.tutorialspoint.com/How-to-get-the-last-element-of-a-list-in-Python
Python sequence, including list object allows indexing. Any element in list can be accessed using zero based index. If index is a negative number, count of inde ...
_________
_________
Sequence Types — list, tuple, range
https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
There are three basic sequence types: lists, tuples, and range objects. Additional sequence types tailored for processing of binary data and text strings are described …
_________
""" 
# Your code should go here:

def lastEle(list1):
    return list1[-1]

print(lastEle([1, 2, 3]))
print(lastEle(["cat", "dog", "duck"]))
print(lastEle([True, False, True]))
print(lastEle([1, "Hello", True]))

# The program is complete.