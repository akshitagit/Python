"""
##Find the Largest Number in a List

Create a function that takes a list of numbers. Return the largest number in the list.


[Examples]

___
findLargestNum([4, 5, 1, 3]) ➞ 5

findLargestNum([300, 200, 600, 150]) ➞ 600

findLargestNum([1000, 1001, 857, 1]) ➞ 1001
_____



[Notes]

___
*) Expect either positive numbers or zero (there are no negative numbers).
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[arrays] [loops] [numbers] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
max() Method
https://www.programiz.com/python-programming/methods/built-in/max
Returns the largest element in an iterable or largest of two or more parameters.
_________
_________
max() Method
https://docs.python.org/3/library/functions.html#max
Return the largest item in an iterable or the largest of two or more arguments.
_________
_________
Aggregations: Min, Max, and Everything In Between
https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html#Minimum-and-Maximum
Similarly, Python has built-in min and max functions, used to find the minimum value and maximum value of any given array.
_________
_________
Python Program to Find Largest Number in a List
https://www.geeksforgeeks.org/python-program-to-find-largest-number-in-a-list/
Given a list of numbers, the task is to write a Python program to find the largest number in given list.
_________
_________
max() Function
https://www.w3schools.com/python/ref_func_max.asp
Returns the item with the highest value, or the item with the highest value in an iterable. If the values are strings, an alphabetically comparison is done.
_________
_________
Video Walk Through the Challenge
https://youtu.be/FfGTh_qm-WU
A video walkthrough of this challenge.
_________
_________
sorted() Function
https://www.geeksforgeeks.org/python-sorted-function/
Returns a sorted list from the iterable object.
_________
""" 
# Your code should go here:

# Expect either positive numbers or zero (there are no negative numbers).
def numMax(list1):
    list1.sort()
    return list1[-1]

def largestNum(list2):
    return max(list2)

print("Using the numMax function.") # Built by using sort and negative indexing method.
print(numMax([1,4,2,5,6,41]))
print(numMax([99,999,999,9999]))
print(numMax([123,1234,13,1,0,0,0]))
print("Using the largestNum function.") # Built by using max() function.
print(largestNum([1,4,2,5,6,41]))
print(largestNum([99,999,999,9999]))
print(largestNum([123,1234,13,1,0,0,0]))

# The program is complete.