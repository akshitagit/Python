"""
##Apocalyptic Numbers

In this challenge, you have to establish if a number is apocalyptic. A positive integer n greater than 0 is apocalyptic when 2 elevated to n contains one or more occurrences of 666 inside it.
Given an integer n, implement a function that returns:
___
*) "Safe" if n is not apocalyptic.
*) "Single" if inside 2^n there's a single occurrence of 666.
*) "Double" if inside 2^n there are two occurrences of 666.
*) "Triple" if inside 2^n there are three occurrences of 666.
___



[Examples]

___
is_apocalyptic(66) ➞ "Safe"
# 2^66 = 73786976294838206464

is_apocalyptic(157) ➞ "Single"
# 2^157 =
# 182687704|666|362864775460604089535377456991567872

is_apocalyptic(220) ➞ "Double"
# 2^220 =
# 168499|666|66969149871|666|8844293872691710232152640 ...

is_apocalyptic(931) ➞ "Triple"
# 2^931 =
# 181520618710|666|8777829|666|135436890332191479738353753001777065257954029122510259245050254290156440857653562895251700406555730694879815558725330603736697259064676478076718090|666| ...
_____



[Notes]

___
*) Any given n will be a positive integer in the range of 1 to 1000.
*) Occurrences have to be unique. You can't use digits that have already been matched again (see example #3, there are five adjacent 6s, but only one possible match).
___



[numbers] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
count() Method
https://www.tutorialspoint.com/python/string_count.htm
Returns the number of occurrences of substring sub in the range [start, end].
_________
_________
Dictionaries
https://realpython.com/python-dicts/
In this Python dictionaries tutorial you'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, yo …
_________
_________
str() Function
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object. In this tutorial, we will learn about Python str() in detail with the help of examples.
_________
_________
How to check if a Python string contains another string?
https://www.educative.io/edpresso/how-to-check-if-python-string-contains-another-string
There are three methods in Python to check if a string contains another string. The method str.find checks if the string contains a substring. If it does, it returns th …
_________
""" 
# Your code should go here:

