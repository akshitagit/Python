"""
####  Remove the Special Characters from a String  ####

Create a function that takes a string, removes all "special" characters (e.g. ., !, @, #, $, %, ^, &, \, *, (, )) and returns the new string. The only non-alphanumeric characters allowed are dashes -, underscores _ and spaces.


[Examples]

___
remove_special_characters("The quick brown fox!") ➞ "The quick brown fox"

remove_special_characters("%fd76$fd(-)6GvKlO.") ➞ "fd76fd-6GvKlO"

remove_special_characters("D0n$c sed 0di0 du1") ➞ "D0nc sed 0di0 du1"
_____



[Notes]

N/A


[arrays] [formatting] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
isalnum() Method
https://www.tutorialspoint.com/python/string_isalnum.htm
Checks whether the string consists of alphanumeric characters.
_________
_________
replace() Method
https://www.tutorialspoint.com/python/string_replace.htm
Returns a copy of the string in which the occurrences of old have been replaced with new, optionally restricting the number of replacements to max.
_________
_________
How would I check a string for a certain letter in Python?
https://stackoverflow.com/questions/4877844/how-would-i-check-a-string-for-a-certain-letter-in-python
How would I tell Python to check the below for the letter x and then print "Yes"? The below is what I have so far... dog = "xdasds" if "x" is in dog: print "Yes!"
_________
_________
Regular Expressions
https://www.tutorialspoint.com/python/python_reg_expressions.htm
A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Re …
_________
_________
Text Constants and Templates
https://pymotw.com/3/string/index.html
The string module dates from the earliest versions of Python. Many of the functions previously implemented in this module have been moved to methods of str objects. The …
_________

"""
#Your code should go here:

