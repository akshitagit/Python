"""
####  ASCII Charts (Part 1: Progress Bar)  ####

Given a character and a value between 0 and 100, return a string that represents a simple progress bar.
___
*) The value represents a percentage.
*) The bar should begin and end with "|"
*) Repeat the character to fill the bar, with each character equivalent to 10%
*) Use spaces to pad the bar to a length of 10 characters.
*) A single space comes after the bar, then a message with the % of completion (e.g. "Progress: 60%")
*) If the value is 100, the message should be "Completed!".
___



[Examples]

___
progress_bar("#", 0) ➞ "|          | Progress: 0%"

progress_bar("=", 40) ➞ "|====      | Progress: 40%"

progress_bar("#", 60) ➞ "|######    | Progress: 60%"

progress_bar(">", 100) ➞ "|>>>>>>>>>>| Completed!"
_____



[Notes]

N/A


[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Formatting Strings with Python
https://stackabuse.com/formatting-strings-with-python/
Sooner or later string formatting becomes a necessary evil for most programmers. More so in the past before the thick client GUI era, but the need to have a specific st …
_________
_________
ljust() Method
https://www.tutorialspoint.com/python/string_ljust
Returns the string left justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if wid …
_________

"""
#Your code should go here:

