"""
##City School Creating IDS

Many IDS (for emails or Google ID) are created using the person's name.
Create a function that will return a four-character ID using the person's first name and last name.
The first character will be the first letter of the first name but in lowercase.
The next three characters will be the first three characters of the last name,
but the first letter will be capitalized and the other two will be in lower case.


[Examples]

___
create_id("mary", "lamb") ➞ "mLam"

create_id("John", "SMITH") ➞ "jSmi"

create_id("mary", "smith") ➞ "mSmi"
_____



[Notes]

There is always one character in the first name and at least three in the last name.


[formatting] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
capitalize() Method
https://www.w3schools.com/python/ref_string_capitalize.asp
Returns a string where the first character is upper case.
_________
_________
string lower() Method
https://www.programiz.com/python-programming/methods/string/lower
Converts all uppercase characters in a string into lowercase characters and returns it.
_________
_________
String title() Method
https://www.programiz.com/python-programming/methods/string/title
Returns a string with first letter of each word capitalized; a title cased string.
_________
""" 
# Your code should go here:

def createID(fName, lName):
    letter1 = fName[0].lower()
    letter2 = lName[0].upper()
    letter3N4 = lName[1:3].lower()
    return letter1+letter2+letter3N4

print(createID("mary", "lamb"))
print(createID("John", "SMITH"))
print(createID("mary", "smith"))
print(createID("Nitkarsh", "Chourasia"))

# The program is complete.