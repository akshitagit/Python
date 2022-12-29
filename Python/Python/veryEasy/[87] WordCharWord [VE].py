"""
##WordCharWord

Create a function that will put the first argument, a character, between every word in the second argument, a string.


[Examples]

___
add("R", "python is fun") ➞ "pythonRisRfun"

add("#", "hello world!") ➞ "hello#world!"

add("#", " ") ➞ "#"
_____



[Notes]

Make sure there are no spaces between words when returning the function.


[formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
replace() Method
https://www.geeksforgeeks.org/python-string-replace/
Is an inbuilt function in Python programming language that returns a copy of the string where all occurrences of a substring is replaced with another substring.
_________
_________
join() Method
https://www.w3schools.com/python/ref_string_join.asp
Takes all items in an iterable and joins them into one string. A string must be specified as the separator.
_________
""" 
# Your code should go here:

replaceMethod = lambda replacer, toBeStr : toBeStr.replace(" ", replacer)


print("\n Replace method outputs: ")
print(replaceMethod("R", "python is fun"))
print(replaceMethod("#", "hello world!"))
print(replaceMethod("#", " "))

# The program is complete.