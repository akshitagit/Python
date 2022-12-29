"""
##Sum of List Less Than 100 List Remix

Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False.


[Examples]

___
list_less_than_100([5, 57]) ➞ True

list_less_than_100([77, 30]) ➞ False

list_less_than_100([0]) ➞ True
_____



[Notes]

N/A


[arrays] [language_fundamentals] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
sum() function
https://www.w3schools.com/python/ref_func_sum.asp
Returns a number, the sum of all items in an iterable.
_________
_________
sum() Function
https://www.geeksforgeeks.org/sum-function-python/
Sums up the numbers in the list.
_________
_________
Comparison Operators
https://data-flair.training/blogs/python-comparison-operators/#:~:text=4.,to%20that%20on%20the%20right.
These are also called relational operators in Python. Along with this, we will learn different types of Comparison Operators in Python: less than, greater than, less t …
_________
""" 
# Your code should go here:

def sumList(list1):
    if sum(list1) < 100:
        return True
    else:
        return False

def sumListFor(list1):
    sum = 0
    for i in list1:
        sum += i
    if sum < 100:
        return True
    else:
        return False

print("sumList function made the sums using the sum() method.")
print(sumList([5, 57]))
print(sumList([77, 30]))
print(sumList([0]))
print(sumList([100]))
print(sumList([99]))
print(sumList([1, 2, 1, 29, 29]))
print("sumlistFor function made the sums using for loop.")
print(sumListFor([5, 57]))
print(sumListFor([77, 30]))
print(sumListFor([0]))
print(sumListFor([100]))
print(sumListFor([99]))
print(sumListFor([1, 2, 1, 29, 29]))

# The program is complete.