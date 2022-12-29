"""
####  Calculated Bonus  ####

A financial institution provides professional services to banks and claims charges from the customers based on the number of man-days provided. Internally, it has set a scheme to motivate and reward staff to meet and exceed targeted billable utilization and revenues by paying a bonus for each day claimed from customers in excess of a threshold target.
This quarterly scheme is calculated with a threshold target of 32 days per quarter, and the incentive payment for each billable day in excess of such threshold target is shown as follows:

Please note that incentive payment is calculated progressively. As an example, if an employee reached total billable days of 45 in a quarter, his/her incentive payment is computed as follows:
___
32*0 + 8*325 + 5*550 = 5350
_____

Write a function to read the billable days of an employee and return the bonus he/she has obtained in that quarter.


[Examples]

___
bonus(15) ➞ 0

bonus(37) ➞ 1625

bonus(50) ➞ 8200
_____



[Notes]

N/A


[conditions] [math] 



-------------------------------------------------------------------
[Resources]
_________
max() Method
https://www.programiz.com/python-programming/methods/built-in/max
Returns the smallest item in an iterable. It can also be used to find the smallest item between two or more parameters.
_________

"""
#Your code should go here:

