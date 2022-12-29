"""
##Make My Way Home

You will be given a list, showing how far James travels away from his home for each day.
He may choose to travel towards or away from his house, so negative values are to be expected.
Create a function that calculates what distance James must walk to get back home.


[Examples]

___
distance_home([2, 4, 2, 5]) ➞ 13

distance_home([-1, -4, -3, -2]) ➞ 10

distance_home([3, 4, -5, -2]) ➞ 0
_____



[Notes]

___
*) Assume James only travels in a straight line.
*) Distance is always a positive number.
___



[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
abs() Function
https://www.geeksforgeeks.org/abs-in-python/
Is used to return the absolute value of a number.
_________
_________
sum() Function
https://www.geeksforgeeks.org/sum-function-python/
Sums up the numbers in the list.
_________
""" 
# Your code should go here:

def distanceHome(distance):
    return abs(sum(distance))

print(distanceHome([2, 4, 2, 5]))
print(distanceHome([-1, -4, -3, -2]))
print(distanceHome([3, 4, -5, -2]))

# The program is complete.