"""
####  The Major Sum  ####

Create a function that takes an integer list and return the biggest between positive sum, negative sum, or 0s count. The major is understood as the greatest absolute.
l = [1,2,3,4,0,0,-3,-2], the function has to return 10, because:
___
*) Positive sum = 1+2+3+4 = 10
*) Negative sum = (-3)+(-2) = -5
*) 0s count = 2 (there are two zeros in list)
___



[Examples]

___
major_sum([1, 2, 3, 4, 0, 0, -3, -2]) ➞ 10

major_sum([-4, -8, -12, -3, 4, 7, 1, 3, 0, 0, 0, 0]) ➞ -27

major_sum([0, 0, 0, 0, 0, 1, 2, -3]) ➞ 5
# Because -3 < 1+2 < 0sCount = 5
_____



[Notes]

___
*) All numbers are integers.
*) There aren't empty lists.
*) All tests are made to return only one value.
___



[arrays] [conditions] [logic] [loops] 



-------------------------------------------------------------------
[Resources]
_________
sum() Function
https://www.geeksforgeeks.org/sum-function-python/
Sum of numbers in the list is required everywhere. Python provide an inbuilt function sum() which sums up the numbers in the list.
_________
_________
max() Function
https://www.jquery-az.com/4-examples-learn-python-max-function/
Is used to return the maximum value for two or more arguments passed to it. If an iterable like a list is passed as an argument, it will return the largest item in the …
_________
_________
Python Conditions
https://www.w3schools.com/python/python_conditions.asp
In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that …
_________

"""
#Your code should go here:

