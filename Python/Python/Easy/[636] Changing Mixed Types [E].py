"""
####  Changing Mixed Types  ####

Create a function that changes all the elements in a list as follows:
___
*) Add 1 to all even integers, nothing to odd integers.
*) Concatenates "!" to all strings and make the first letter of the word a capital letter.
*) Changes all boolean values to its opposite.
___



[Examples]

___
change_types(["a", 12, True]) ➞ ["A!", 13, False]

change_types([13, "13", "12", "twelve"]) ➞ [13, "13!", "12!", "Twelve!"]

change_types([False, "False", "true"]) ➞ [True, "False!", "True!"]
_____



[Notes]

___
*) There won't be any float values.
*) You won't get strings with both numbers and letters in them.
*) Although the task may be easy, try keeping your code as clean and as readable as possible!
___



[arrays] [conditions] 



-------------------------------------------------------------------
[Resources]
_________
capitalize() Method
https://www.geeksforgeeks.org/string-capitalize-python/
Converts the first character of a string to capital (uppercase) letter. If the string has its first character as capital, then it returns the original string.
_________
_________
type() and isinstance()
https://www.geeksforgeeks.org/type-isinstance-python/
Python has a built-in method called as type which generally come in handy while figuring out the type of variable used in the program in the runtime. If a single argume …
_________
_________
enumerate()
http://book.pythontips.com/en/latest/enumerate.html
It allows us to loop over something and have an automatic counter.
_________

"""
#Your code should go here:

