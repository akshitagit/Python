"""
####  Encoded String Parse  ####

Create a function which takes in an encoded string and returns a dictionary according to the following example:


[Examples]

___
parse_code("John000Doe000123") ➞ {
  "first_name": "John",
  "last_name": "Doe",
  "id": "123"
}

parse_code("michael0smith004331") ➞ {
  "first_name": "michael",
  "last_name": "smith",
  "id": "4331"
}

parse_code("Thomas00LEE0000043") ➞ {
  "first_name": "Thomas",
  "last_name": "LEE",
  "id": "43"
}
_____



[Notes]

___
*) The string will always be in the same format: first name, last name and id with zeros between them.
*) id numbers will not contain any zeros.
*) Bonus: Try solving this using RegEx.
___



[formatting] [objects] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
join() Method
https://www.w3schools.com/python/ref_string_join.asp
Takes all items in an iterable and joins them into one string. A string must be specified as the separator. x = "#".join(myTuple) print(x)
_________
_________
Regex Tester and Debugger
https://regex101.com
With highlighting for PHP, PCRE, Python, Golang and JavaScript.
_________
_________
Convert List to Dictionary
https://careerkarma.com/blog/python-convert-list-to-dictionary/
Learn how to convert a list to a dictionary using dictionary comprehension, the dict.fromkeys() method, and the zip() function.
_________
_________
split() Method
https://www.w3schools.com/python/ref_string_split.asp
Splits a string into a list. You can specify the separator, default separator is any whitespace.
_________
_________
Split strings
https://note.nkmk.me/en/python-split-rsplit-splitlines-re/
Here's how to split strings by delimiters, line breaks, regular expressions, and the number of characters in Python.
_________

"""
#Your code should go here:

