"""
####  Strange Pair  ####

A pair of strings form a strange pair if both of the following are true:
___
*) The 1st string's first letter = 2nd string's last letter.
*) The 1st string's last letter = 2nd string's first letter.
___

Create a function that returns True if a pair of strings constitutes a strange pair, and False otherwise.


[Examples]

___
is_strange_pair("ratio", "orator") ➞ True
# "ratio" ends with "o" and "orator" starts with "o".
# "ratio" starts with "r" and "orator" ends with "r".

is_strange_pair("sparkling", "groups") ➞ True

is_strange_pair("bush", "hubris") ➞ False

is_strange_pair("", "") ➞ True
_____



[Notes]

It should work on a pair of empty strings (they trivially share nothing).


[language_fundamentals] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Ternary Operator
https://www.geeksforgeeks.org/ternary-operator-in-python/
Are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. It simply allows to test a condition in a single …
_________
_________
How to Index and Slice Strings
https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
The Python string data type is a sequence made up of one or more individual characters consisting of letters, numbers, whitespace characters, or symbols. Strings are se …
_________

"""
#Your code should go here:

