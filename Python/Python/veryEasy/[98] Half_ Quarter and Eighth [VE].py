"""
##Half, Quarter and Eighth

Create a function that takes a number and return a list of three numbers: half of the number, quarter of the number and an eighth of the number.


[Examples]

___
half_quarter_eighth(6) ➞ [3, 1.5, 0.75]

half_quarter_eighth(22) ➞ [11, 5.5, 2.75]

half_quarter_eighth(25) ➞ [12.5, 6.25, 3.125]
_____



[Notes]

The order of the list is: half, quarter, eighth.


[arrays] [math] 



-------------------------------------------------------------------
[Resources]
_________
Video Walk Through the Challenge
https://youtube.com/watch?v=_HKaYYyrahI
A video walkthrough of this challenge.
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
_________
_________
append() Method
https://www.w3schools.com/python/ref_list_append.asp
Appends an element to the end of the list.
_________
""" 
# Your code should go here:

def halfQuarterEight(num1):
    half = num1 / 2
    quarter = num1 / 4
    eighth = num1 / 8
    return half, quarter, eighth

halfQuarterEight1 = lambda num1 : ((num1 / 2), (num1 / 4), (num1 / 8))

print(halfQuarterEight(6))
print(halfQuarterEight(22))
print(halfQuarterEight(25))
print(halfQuarterEight1(6))
print(halfQuarterEight1(22))
print(halfQuarterEight1(25))

# The program is complete.