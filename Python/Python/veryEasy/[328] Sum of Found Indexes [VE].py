"""
##Sum of Found Indexes

Create a function which takes in a list of numbers and a number to find. Return the sum of every index in the list which matches the chosen number.


[Examples]

___
sum_found_indexes([0, 3, 3, 0, 0, 3], 3) ➞ 8
# The number 3 was found at indexes 1, 2 and 5.
# 8 = 1 + 2 + 5

sum_found_indexes([1, 2, 3, 4, 5, 6], 3) ➞ 2

sum_found_indexes([100, 100, 100, 100, 100], 100) ➞ 10

sum_found_indexes([5, 10, 15, 20], 2) ➞ 0
_____



[Notes]

0 can be the result if no number in the list matches or if the only matching element is at index 0.


[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
How to find all occurrences of an element in a list?
https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
index() will just give the first occurrence of an item in a list. Is there a neat trick which returns all indices in a list?
_________
_________
How to find char in string and get all the indexes?
https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes
I got some simple code. The function only return the first index. If I change return to print, it will print 0 0 0. Why is this and is there any way to get 0 1 2?
_________
_________
How to sum a list of numbers in Python?
https://stackoverflow.com/questions/4362586/sum-a-list-of-numbers-in-python
I have a list of numbers such as [1,2,3,4,5...], and I want to calculate (1+2)/2 and for the second, (2+3)/2 and the third, (3+4)/2, and so on. How can I do that? I wou …
_________
""" 
# Your code should go here:

