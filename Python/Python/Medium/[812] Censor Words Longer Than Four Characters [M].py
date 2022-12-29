"""
####  Censor Words Longer Than Four Characters  ####

Create a function that takes a string and censors words over four characters with *.


[Examples]

___
censor("The code is fourty") ➞ "The code is ******"

censor("Two plus three is five") ➞ "Two plus ***** is five"

censor("aaaa aaaaa 1234 12345") ➞ "aaaa ***** 1234 *****"
_____



[Notes]

___
*) Don't censor words with exactly four characters.
*) If all words have four characters or less, return the original string.
*) The amount of * is the same as the length of the word.
___



[conditions] [strings] 



-------------------------------------------------------------------
[Resources]
_________
len() Method
https://www.w3schools.com/python/ref_func_len.asp
Find the length of words.
_________
_________
join() Method
https://www.w3schools.com/python/ref_string_join.asp
Join all items in a tuple into a string, using a hash character as separator.
_________
_________
split() Method
https://www.w3schools.com/python/ref_string_split.asp
Splits a string into a list.
_________
_________
str.replace(old, new)
https://python-reference.readthedocs.io/en/latest/docs/str/replace.html
Returns a copy of the string with a specified substring replaced specified number of times.
_________

"""
#Your code should go here:

