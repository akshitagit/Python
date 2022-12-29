"""
####  Letter Occurrences Per Word  ####

Create a function that takes in a sentence and a character to find. Return a dictionary of each word in the sentence, with the number of the specified character as the value.


[Examples]

___
find_occurrences("Hello World", "o") ➞ {
  "hello" : 1,
  "world" : 1
}

find_occurrences("Create a nice JUICY function", "c") ➞  {
  "create" : 1,
  "a" : 0,
  "nice" : 1,
  "juicy" : 1,
  "function" : 1
}

find_occurrences("An APPLE a day keeps an Archeologist AWAY...", "A") ➞ {
  "an" : 1,
  "apple" : 1,
  "a" : 1,
  "day" : 1,
  "keeps" : 0,
  "archeologist" : 1,
  "away..." : 2
}
_____



[Notes]

___
*) The function shouldn't be case sensitive.
*) Words in the dictionary should be in lowercase.
*) You may be required to find punctuation.
*) Duplicate words should be ignored (see example #3 for the word "an").
___



[algorithms] [arrays] [data_structures] 



-------------------------------------------------------------------
[Resources]
_________
String lower() Method
https://www.programiz.com/python-programming/methods/string/lower
Converts all uppercase characters in a string into lowercase characters and returns it.
_________
_________
split() Method
https://www.programiz.com/python-programming/methods/string/split
Breaks up a string at the specified separator and returns a list of strings.
_________
_________
String count() Method
https://www.programiz.com/python-programming/methods/string/count
Returns the number of occurrences of a substring in the given string.
_________
_________
Find the Occurrence of Each Character in String
https://www.revisitclass.com/python/find-the-occurrence-of-each-character-in-string-using-python/
The count function is used to count the occurrence of each character in a string. Here we can give the specific character in count function and it will return the numbe …
_________

"""
#Your code should go here:

