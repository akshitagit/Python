"""
##Length of Worm

Given a string worm create a function that takes the length of the worm and converts it into millimeters. Each - represents one centimeter.


[Examples]

___
worm_length("----------") ➞ "100 mm."

worm_length("") ➞ "invalid"

worm_length("---_-___---_") ➞ "invalid"
_____



[Notes]

Return "invalid" if an empty string is given or if the string has characters other than -.


[strings] 



-------------------------------------------------------------------
[Resources]
_________
Centimeters to Millimeters Conversion
https://www.rapidtables.com/convert/length/cm-to-mm.html
How to convert from centimeters to millimeters.
_________
_________
How to Create a Set
https://www.w3schools.com/python/python_sets.asp
How to create a set that can be searched in Python.
_________
""" 
# Your code should go here:

def wormLength(length):
    a = []
    for i in length:
        if i != "-":
            # print("Invalid characters found.")
            a.append("invalid")
            break
        a.append(i)
    if len(a) <=0:
        return "invalid, length cannot be zero."
    elif "invalid" in a:
        return "Invalid characters found."
    else:
        return "{} mm".format(len(a) * 10)

print(wormLength("-----"))
print(wormLength("----------"))
print(wormLength(""))
print(wormLength("123"))
print(wormLength("-----________--------"))
print(wormLength("----__-_-_---"))

# The program is complete.