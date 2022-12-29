"""
####  RNA Reverse Complement  ####

Create a function that finds the reverse complement of a ribonucleic acid (RNA) strand. The RNA will be represented as a string containing only the characters "A", "C", "G" and "U". Since RNA can only (canonically) allow pairings of A/U and G/C, the complement of an RNA would be as follows:
___
original -> complement
"AAA" -> "UUU"
"UUU" -> "AAA"
"GGG" -> "CCC"
"CCC" -> "GGG"
"GGAACC" -> "CCUUGG"
_____

Your function should find the complement on the right AND also reverse the resulting string.


[Examples]

___
reverse_complement("GUGU") ➞ "ACAC"

reverse_complement("UCUCG") ➞ "CGAGA"

reverse_complement("CAGGU") ➞ "ACCUG"
_____



[Notes]

Assume all input seqeuences are valid.


[algorithms] [loops] 



-------------------------------------------------------------------
[Resources]
_________
String maketrans() Method
https://www.programiz.com/python-programming/methods/string/maketrans
Returns a mapping table for translation usable for translate() method.
_________
_________
String translate() Method
https://www.programiz.com/python-programming/methods/string/translate
Returns a string where each character is mapped to its corresponding character in the translation table.
_________
_________
Reverse String
https://www.journaldev.com/23647/python-reverse-string
Can be done using slicing, str.join() function, reversed() function, for loop, while loop. There is no reverse() function in string.
_________
_________
maketrans() and translate() Functions
https://www.geeksforgeeks.org/python-maketrans-translate-functions/
Is used to construct the transition table i.e specify the list of characters that need to be replaced in the whole string or the characters that need to be deleted from …
_________

"""
#Your code should go here:

