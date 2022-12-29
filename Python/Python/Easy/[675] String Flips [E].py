"""
####  String Flips  ####

Create a function that takes a string as the first argument, and a (string) specification as a second argument. If the specification is "word", return a string with each word reversed while maintaining their original order. If the specification is "sentence", reverse the order of the words in the string, while keeping the words intact.


[Examples]

___
txt = "There's never enough time to do all the nothing you want"


flip("Hello", "word") ➞ "olleH"

flip("Hello", "sentence") ➞ "Hello"

flip(txt, "word") ➞ "s'erehT reven hguone emit ot od lla eht gnihton uoy tnaw"

flip(txt, "sentence") ➞ "want you nothing the all do to time enough never There's"
_____



[Notes]

N/A


[language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
split() Method
https://www.geeksforgeeks.org/python-string-split/
Returns a list of strings after breaking the given string by the specified separator.
_________
_________
join() Method
https://www.geeksforgeeks.org/join-function-python/
Returns a string in which the elements of sequence have been joined by str separator.
_________
_________
How to Reverse a String in Python
https://www.w3schools.com/python/python_howto_reverse_string.asp
In this particular example, the slice statement [::-1] is the same as [11:0:-1] which means start at position 11  (because "Hello "World" has 11 characters), end at p …
_________

"""
#Your code should go here:

