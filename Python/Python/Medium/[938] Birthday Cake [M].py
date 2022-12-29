"""
####  Birthday Cake  ####

Create a function which constructs a rectangular birthday cake, based on someone's name and age! Build it out of strings in a list and make sure to surround the birthday message with the character that fits the rule:
___
*) If the age is an even number, surround the message with "#".
*) If the age is an odd number, surround the message with "*".
___

Other important rules:
___
*) The message should be in the format: {age} Happy Birthday {name}! {age}
*) Leave a space between the edge of the cake and the age numbers.
___



[Examples]

___
get_birthday_cake("Jack", 10) ➞ [
  "##############################",
  "# 10 Happy Birthday Jack! 10 #",
  "##############################"
]

get_birthday_cake("Russell", 19) ➞ [
  "*********************************",
  "* 19 Happy Birthday Russell! 19 *",
  "*********************************"
]

get_birthday_cake("Isabelle", 2) ➞ [
  "################################",
  "# 2 Happy Birthday Isabelle! 2 #",
  "################################"
]
_____



[Notes]

The amount of characters in the banner should be the same length as the message to pass the tests.


[arrays] [formatting] 



-------------------------------------------------------------------
[Resources]
_________
Using % and .format() for great good!
https://pyformat.info
Using % and .format() for great good!
_________
_________
Python String format() Method
https://www.w3schools.com/python/ref_string_format.asp
Formats the specified value(s) and inserts them inside the string's placeholder.
_________

"""
#Your code should go here:

