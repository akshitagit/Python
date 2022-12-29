"""
##Iterable Unpacking

There is an easy way to assign to array values to the nth index by using the Rest element.
___
head, tail = [1, 2, 3, 4]

print(head) ➞ 1
print(tail) ➞ 2
_____

But how could I make tail = [2, 3, 4] instead of tail = 2? Add something into the code and make this happen.


[Notes]

Check the Resources tab for more examples.


[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Packing and Unpacking Arguments in Python
https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
We use two operators * (for tuples) and ** (for dictionaries). Consider a situation where we have a function that receives four arguments. We want to make call to this …
_________
_________
List Unpacking
https://note.nkmk.me/en/python-tuple-list-unpack/
In Python, elements of tuples and lists can be assigned to multiple variables. It is called sequence unpacking.
_________
_________
Getting Started with Sequence Unpacking in Python
https://levelup.gitconnected.com/how-to-unpack-sequences-in-python-8b3c0e6ef4fa
Tuples are specified with parenthesis and they are a sequence of immutable python objects. This simply means that, unlike with lists, you can’t do element-wise assignme …
_________
""" 
# Your code should go here:

def iterUnpack():
    list1 = range(1,10)
    head, *tail = list1
    print(head)
    print(tail)

iterUnpack()

# The program is complete.