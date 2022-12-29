"""
####  How Many Days Between Two Dates  ####

Create a function get_days that takes two dates and returns the number of days between the first and second date.


[Examples]

___
get_days(
  datetime.date(2019, 6, 14),  # June 14, 2019
  datetime.date(2019, 6, 20)  # June 20, 2019
) ➞ 6


get_days(
  datetime.date(2018, 12, 29),  # December 29, 2018
  datetime.date(2019, 1, 1)  # January 1, 2019
) ➞ 3
# Dates may not all be in the same month/year.


get_days(
  datetime.date(2020, 5, 24),
  datetime.date(2019, 5, 24))
) ➞ -366
# Backwards dates should return a negative change.
_____



[Notes]

N/A


[dates] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Basic Date and Time Types
https://docs.python.org/3/library/datetime.html#datetime.timedelta
While date and time arithmetic is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation.
_________
_________
Difference Between Two Dates (In Minutes) Using datetime.timedelta() Method
https://www.geeksforgeeks.org/python-difference-between-two-dates-in-minutes-using-datetime-timedelta-method/
To find the difference between two dates in Python, one can use the timedelta class which is present in the datetime library. The timedelta class stores the difference …
_________
_________
Subtract Datetime
https://www.delftstack.com/howto/python/python-datetime-subtraction/
Examples of subtracting dates from each other.
_________
_________
Timedelta
https://docs.python.org/2/library/datetime.html#date-objects
The datetime2 is a duration of timedelta removed from datetime1, moving forward in time if timedelta.days > 0, or backward if timedelta.days < 0. The result has the sam …
_________

"""
#Your code should go here:

