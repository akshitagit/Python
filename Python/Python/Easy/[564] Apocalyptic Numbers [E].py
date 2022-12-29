"""
##Apocalyptic Numbers

A number n is apocalyptic if 2^n contains a string of 3 consecutive 6s (666 being the presumptive "number of the beast").
Create a function that takes a number n as input. If the number is apocalyptic, find the index of 666 in 2^n, and return "Repent! X days until the Apocalypse!" (X being the index). If not, return "Crisis averted. Resume sinning.".


[Examples]

___
apocalyptic(109) ➞ "Crisis averted. Resume sinning."

apocalyptic(157) ➞ "Repent! 9 days until the Apocalypse!"
# 2^157 -> 182687704666362864775460604089535377456991567872
# 666 at 10th position (index 9)

apocalyptic(175) ➞ "Crisis averted. Resume sinning."

apocalyptic(220) ➞ "Repent! 6 days until the Apocalypse!"
_____



[Notes]

N/A


[math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
find() Method
https://www.geeksforgeeks.org/string-find-python/
Returns the lowest index of the substring if it is found in given string. If its is not found then it returns -1.
_________
_________
format() string Method
https://www.w3schools.com/python/ref_string_format.asp
Formats the specified value(s) and insert them inside the string's placeholder. syntax --> string.format(value1, value2...)
_________
_________
How to check if a Python string contains another string?
https://www.afternerd.com/blog/python-string-contains/
One of the most common operations that programmers use on strings is to check whether a string contains some other string.
_________
_________
Difference between find and index?
https://stackoverflow.com/questions/22190064/difference-between-find-and-index
I am new to python and cannot quite understand the difference between find and index.
_________
""" 
# Your code should go here:

