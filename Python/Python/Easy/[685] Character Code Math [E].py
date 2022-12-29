"""
####  Character Code Math  ####

Turn each character in a string s into its ASCII character code and join them together to create a number.
For example, for string "abc", the number is 979899. We will call this number "num1".
___
"abc" ➞ "a" = 97, "b" = 98, "c" = 99 ➞ 979899
_____

Then replace any incidence of the number 7 with the number 1, and call this number "num2":
___
num1 = 979899

num2 = 919899
_____

Return the difference between the sum of the digits in num1 and num2:
___
  (9 + 7 + 9 + 8 + 9 + 9)
- (9 + 1 + 9 + 8 + 9 + 9)
-------------------------
         ➞  6
_____



[Examples]

___
calc("ABCDabcd") ➞ 12

calc("cdefgh") ➞ 0

calc("ifkhchlhfde") ➞ 6
_____



[Notes]

Lowercase and uppercase characters have different ASCII character codes.


[algorithms] [language_fundamentals] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
ord() Function
https://www.w3schools.com/python/ref_func_ord.asp
Returns the number representing the unicode code of a specified character.
_________
_________
len() Function
https://www.w3schools.com/python/ref_func_len.asp
Returns the number of items in an object.
_________
_________
join() Method
https://www.w3schools.com/python/ref_string_join.asp
Takes all items in an iterable and joins them into one string.
_________
_________
str() Function
https://www.w3schools.com/python/ref_func_str.asp
Converts the specified value into a string.
_________
_________
How to Use the Count() Function
https://www.askpython.com/python/string/python-count-method
Python String has got an in-built function – string.count() method to count the occurrence of a character or a substring in the particular input string. The string.cou …
_________

"""
#Your code should go here:

