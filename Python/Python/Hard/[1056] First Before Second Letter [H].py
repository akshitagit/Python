"""
####  First Before Second Letter  ####

You are given three inputs: a string, one letter, and a second letter.
Write a function that returns True if every instance of the first letter occurs before every instance of the second letter.


[Examples]

___
first_before_second("a rabbit jumps joyfully", "a", "j") ➞ True
# Every instance of "a" occurs before every instance of "j".

first_before_second("knaves knew about waterfalls", "k", "w") ➞  True

first_before_second("happy birthday", "a", "y") ➞ False
# The "a" in "birthday" occurs after the "y" in "happy".

first_before_second("precarious kangaroos", "k", "a") ➞ False
_____



[Notes]

___
*) All strings will be in lower case.
*) All strings will contain the first and second letters at least once.
___



[strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
rfind() Method
https://www.geeksforgeeks.org/python-string-rfind/#targetText=Python%20String%20%7C%20rfind(),found%20then%20it%20returns%20-1.&targetText=Parameters%20%3A,searched%20in%20the%20given%20string.
Returns the highest index of the substring if found in given string. If not found then it returns -1.
_________
_________
Count Occurrences of a Character in String
https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/
Given a string, the task is to count the frequency of a single character in that string. This particular operation on string is quite useful in many applications such a …
_________
_________
rindex() Method
https://www.tutorialspoint.com/python3/string_rindex.htm
Returns the last index where the substring str is found, or raises an exception if no such index exists, optionally restricting the search to string[beg:end].
_________

"""
#Your code should go here:

