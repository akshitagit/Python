"""
##Compare Strings by Count of Characters

Create a function that takes two strings as arguments and return either True or False depending on whether the total
number of characters in the first string is equal to the total number of characters in the second string.


[Examples]

___
comp("AB", "CD") ➞ True

comp("ABC", "DE") ➞ False

comp("hello", "edabit") ➞ False
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[conditions] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Python Strings
https://thepythonguru.com/python-strings/
The length variable is applicable to array but not for string objects whereas the length() method is applicable for string objects but not for arrays.
_________
_________
The Length of a string len() Function
https://www.tutorialspoint.com/python3/string_len.htm
Returns the length of the string.
_________
_________
len() Method
https://www.guru99.com/python-string-length-len.html#:~:text=len()%20is%20a%20built,provide%20the%20number%20of%20elements.
Is a built-in function in python. You can use the len() to get the length of the given string, array, list, tuple, dictionary, etc. You can use len function to optimize …
_________
""" 
# Your code should go here:

def len2Str(str1, str2):
    if (len(str1) == len(str2)):
        return True
    else:
        return False

print(len2Str("123", "568"))
print(len2Str("000", "123"))
print(len2Str("ABC","YE"))
print(len2Str("dasf", "asd"))

# The program is complete.