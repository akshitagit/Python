"""
##How Many D's Are There?

Create a function that counts how many D's are in a sentence.


[Examples]

___
count_d("My friend Dylan got distracted in school.") ➞ 4

count_d("Debris was scattered all over the yard.") ➞ 3

count_d("The rodents hibernated in their den.") ➞ 3
_____



[Notes]

___
*) Your function must be case-insensitive.
*) Remember to return the result.
*) Check the Resources for help.
___



[algorithms] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
string lower() Method
https://www.programiz.com/python-programming/methods/string/lower
Converts all uppercase characters in a string into lowercase characters and returns it.
_________
_________
string count() Method
https://www.programiz.com/python-programming/methods/string/count
Returns the number of occurrences of a substring in the given string.
_________
""" 
# Your code should go here:

def countD(str1):
    return (str1.lower()).count('d')

print(countD("d"))
print(countD("ddDDd"))
print(countD("My friend Dylan got distracted in school."))
print(countD("Debris was scattered all over the yard."))
print(countD("The rodents hibernated in their den."))

# The program is complete.