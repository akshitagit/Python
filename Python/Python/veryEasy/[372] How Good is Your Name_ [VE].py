"""
##How Good is Your Name?

Create a function that takes a string of name and checks how much good is the given name. A preloaded dictionary of alphabet scores is available in the Code tab. Add up the letters of your name to get the total score.
___
scores = {"A": 100, "B": 14, "C": 9, "D": 28, "E": 145, "F": 12, "G": 3,
          "H": 10, "I": 200, "J": 100, "K": 114, "L": 100, "M": 25,
          "N": 450, "O": 80, "P": 2, "Q": 12, "R": 400, "S": 113,
          "T": 405, "U": 11, "V": 10, "W": 10, "X": 3, "Y": 210, "Z": 23}
_____

Return your result as per the following rules:
___
score <= 60:   "NOT TOO GOOD"

61 <= score <= 300:  "PRETTY GOOD"

301 <= score <= 599:  "VERY GOOD"

score >= 600:  "THE BEST"
_____



[Examples]

___
name_score("MUBASHIR") ➞ "THE BEST"

name_score("YOU") ➞ "VERY GOOD"

name_score("MATT") ➞ "THE BEST"

name_score("PUBG") ➞ "NOT TOO GOOD"
_____



[Notes]

N/A


[interview] [language_fundamentals] [objects] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Conditions and If Statements
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics. These conditions can be used in several ways, most commonly in "if statements" and loops. An "if stateme …
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Operators are used to perform operations on variables and values. In the example below, we use the + operator to add together two values.
_________
_________
String replace() Method
https://www.geeksforgeeks.org/python-string-replace/
Returns a copy of the string where all occurrences of a substring is replaced with another substring.
_________
_________
String upper() Method
https://www.geeksforgeeks.org/python-string-upper/
Converts all lowercase characters in a string into uppercase characters and returns it.
_________
_________
Loop Dictionaries
https://www.w3schools.com/python/python_dictionaries_loop.asp
You can loop through a dictionary by using a for loop. When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to ret …
_________
_________
For Loops
https://www.w3schools.com/python/python_for_loops.asp
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other program …
_________
_________
Python Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp
Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is unordered, changeable and does not allow duplicates. Dictionaries …
_________
_________
How to Reference Values in a Dict
https://www.tutorialspoint.com/python/python_dictionary.htm
Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any …
_________
""" 
# Your code should go here:

