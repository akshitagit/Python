"""
##Find the Smallest Number in a List

Create a function that takes a list of numbers and returns the smallest number in the list.


[Examples]

___
find_smallest_num([34, 15, 88, 2]) ➞ 2

find_smallest_num([34, -345, -1, 100]) ➞ -345

find_smallest_num([-76, 1.345, 1, 0]) ➞ -76

find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]) ➞ -0.9999

find_smallest_num([7, 7, 7]) ➞ 7
_____



[Notes]

___
*) Test cases contain decimals.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[arrays] [loops] [numbers] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
min() Method
https://www.programiz.com/python-programming/methods/built-in/min
Returns the smallest element in an iterable or smallest of two or more parameters.
_________
_________
Finding the Largest and Smallest Number
http://programminginpython.com/python-program-largest-smallest-number-list/
A simple python program to find the smallest and largest element in a list. Here we use 2 functions max() and min() to find the largest and smallest number.
_________
_________
Python Program To Find The Biggest & Smallest of 3 Numbers
https://medium.com/programminginpython-com/python-program-to-find-the-biggest-and-smallest-of-3-numbers-using-lists-6a1a32119f0e
Here we discuss a simple python program which finds the biggest and smallest number out of given three numbers. Here we use python lists in this program. Here we add th …
_________
_________
min() Function
https://www.w3schools.com/python/ref_func_min.asp
Returns the item with the lowest value, or the item with the lowest value in an iterable. If the values are strings, an alphabetically comparison is done.
_________
_________
min() Function
https://www.geeksforgeeks.org/python-min-function/
Finds the minimum value in a list.
_________
_________
sort() List Method
https://www.freecodecamp.org/news/python-sort-how-to-sort-a-list-in-python/
Learn a different way of performing sorting in Python by using the sorted() function so you can see how it differs from sort(). By the end, you will know the basics of …
_________
""" 
# Your code should go here:

def numMin(list1):
    list1.sort(reverse=True)
    return list1[-1]

def smallestNum(list2):
    return min(list2)

print("Using the numMin function.") # Built by using sort(reverse=True) and negative indexing method.
print(numMin([1,4,2,5,6,41]))
print(numMin([99,999,999,9999]))
print(numMin([123,1234,13,1,0,0,0]))
print("Using the smallestNum function.") # Built by using min() function.
print(smallestNum([1,4,2,5,6,41]))
print(smallestNum([99,999,999,9999]))
print(smallestNum([123,1234,13,1,0,0,0]))

# The program is Complete.