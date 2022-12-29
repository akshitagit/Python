"""
##Is the String Odd or Even?

Given a string, return True if its length is even or False if the length is odd.


[Examples]

___
odd_or_even("apples") ➞ True
# The word "apples" has 6 characters.
# 6 is an even number, so the program outputs True.

odd_or_even("pears") ➞ False
# "pears" has 5 letters, and 5 is odd.
# Therefore the program outputs False.

odd_or_even("cherry") ➞ True
_____



[Notes]

N/A


[conditions] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
len() Function
https://www.geeksforgeeks.org/python-string-length-len/
Is an inbuilt function in Python programming language that returns the length of the string.
_________
_________
Truthy and Falsy Values
https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/#:~:text=You%20can%20check%20if%20a,one%20of%20True%20or%20False%20.
What true and false values are. What makes a value true or false. How to use the bool() function to determine if a value is true or false. How to make objects from user …
_________
_________
Check if Number is Odd or Even
https://www.javatpoint.com/python-check-number-is-odd-or-even
If you divide a number by 2 and it gives a remainder of 0 then it is known as even number, otherwise an odd number.
_________
_________
What Is a Modulo Operator (%)?
https://www.geeksforgeeks.org/what-is-a-modulo-operator-in-python/
When we see a ‘%’ the first thing that comes to our mind is the “Percentage-sign”, but when we think of it from the perspective of computer language, this sign has, in …
_________
""" 
# Your code should go here:

def lenStrBool(str1):
    if (len(str1) % 2 == 0):
        return True
    else:
        return False

print(lenStrBool("apples"))
print(lenStrBool("pears"))
print(lenStrBool("Nitkarsh"))
print(lenStrBool("NitkarshChourasia"))

# The program is complete.