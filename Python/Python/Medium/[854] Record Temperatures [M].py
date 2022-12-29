"""
####  Record Temperatures  ####

You are given two lists that each contain data that represents the min and max weather temperatures for each day of the week.
The records list contains the all-time record low/high temperatures for that day of the week.
___
[[record low, record high], ...]
_____

The current week list contains the daily low/high temperatures for each day of the current week.
___
[[daily low, daily high], ...]
_____

A daily high temperature is considered a new record high if it is higher than the record high for that day of the week. A daily low temperature is considered a new record low if it is lower than the record low for that day of the week.
Compare the daily low/high temperatures of the current week to the record lows/highs and return a list with the updated record temperatures.
___
*) There may be multiple record temperatures in a week.
*) If there are no broken records return the original records list.
___



[Example]

___
#             sun       mon      tues       wed      thur      fri       sat
record_temps([[34, 82], [24, 82], [20, 89],  [5, 88],  [9, 88], [26, 89], [27, 83]],
            [[44, 72], [19, 70], [40, 69], [39, 68], [33, 64], [36, 70], [38, 69]])

➞           [[34, 82], [19, 82], [20, 89], [5, 88], [9, 88], [26, 89], [27, 83]]
_____

The previous record low for Monday was 24. The current week's low for Monday was 19. So 19 replaces 24 as Monday's new record low.


[Notes]

___
*) There won't be a record high and record low set on the same day.
*) Index 0 will always be the low and index 1 will always be the high [low, high].
*) For reference these temps are °F but you do not need to convert any temperatures.
___



[arrays] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Simplify Looping With Counters
https://realpython.com/python-enumerate/
Once you learn about for loops in Python, you know that using an index to access items in a sequence isn't very Pythonic. So what do you do when you need that index val …
_________
_________
min() Function
https://www.w3schools.com/python/ref_func_min.asp
Returns the item with the lowest value, or the item with the lowest value in an iterable.
_________
_________
max() Function
https://www.w3schools.com/python/ref_func_max.asp
Returns the item with the highest value, or the item with the highest value in an iterable.
_________
_________
zip() Function
https://www.w3schools.com/python/ref_func_zip.asp
Returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator a …
_________

"""
#Your code should go here:

