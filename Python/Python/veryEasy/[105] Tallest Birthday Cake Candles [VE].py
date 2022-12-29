"""
##Tallest Birthday Cake Candles

You are in charge of the cake for a child's birthday.
You have decided the cake will have one candle for each year of their total age.
They will only be able to blow out the tallest of the candles. Count how many candles are tallest.


[Examples]

___
birthday_cake_candles([4, 4, 1, 3]) ➞ 2
# The maximum height candles are four units high.
# There are two of them, so you return 2.

birthday_cake_candles([3, 2, 1, 3]) ➞ 2

birthday_cake_candles([82, 49, 82, 82, 41, 82, 15, 63, 38, 25]) ➞ 4
_____



[Notes]

N/A


[arrays] 



-------------------------------------------------------------------
[Resources]
_________
List count() Method
https://www.w3schools.com/python/ref_list_count.asp
Returns the number of elements with the specified value.
_________
_________
max() Method
https://www.w3schools.com/python/ref_func_max.asp
Returns the item with the highest value, or the item with the highest value in an iterable. If the values are strings, an alphabetically comparison is done.
_________
""" 
# Your code should go here:

def birthdayCakeCandles(list1):
    return list1.count(max(list1))

print(birthdayCakeCandles([3, 2, 1, 3]))
print(birthdayCakeCandles([82, 49, 82, 82, 41, 82, 15, 63, 38, 25]))

# The program is complete.