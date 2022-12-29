"""
##Fix the Error: Vowel Edition

Your friend is trying to write a function that removes all vowels from a string. They write:
___
def remove_vowels(string):
    vowels = "aeiou"
    for vowel in vowels[1]:
        string.replace(vowel, "", 1)
    return string
_____

However, it seems that it doesn't work? Fix your friend's code so that it actually does remove all vowels.


[Examples]

___
remove_vowels("ben") ➞ "bn"

remove_vowels("hello") ➞ "hllo"
# The "e" is removed, but the "o" is still there!

remove_vowels("apple") ➞ "appl"
# The "e" is removed, but the "a" is still there!
_____



[Notes]

All letters will be lowercase.


[bugs] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to remove the vowels from a string in Python?
https://stackoverflow.com/questions/21581824/correct-code-to-remove-the-vowels-from-a-string-in-python
I'm pretty sure my code is correct but it doesn't seem to returning the expected output: input anti_vowel("Hey look words") --> outputs: "Hey lk wrds". Apparently it's …
_________
_________
replace() Method
https://www.tutorialspoint.com/python/string_replace.htm
Returns a copy of the string in which the occurrences of old have been replaced with new, optionally restricting the number of replacements to max.
_________
""" 
# Your code should go here:

