"""
##Luke, I Am Your ...

Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.



[Examples]

___
relation_to_luke("Darth Vader") ➞ "Luke, I am your father."

relation_to_luke("Leia") ➞ "Luke, I am your sister."

relation_to_luke("Han") ➞ "Luke, I am your brother in law."
_____



[Notes]

N/A


[conditions] [formatting] [objects] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Dictionaries
https://realpython.com/python-dicts/
Python provides another composite data type called a dictionary, which is similar to a list in that it is a collection of objects. Here’s what you’ll learn in this tut …
_________
_________
Dictionary
https://www.w3schools.com/python/python_dictionaries.asp
Is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
_________
_________
Check if a Key Exists
https://able.bio/rhett/check-if-a-key-exists-in-a-python-dictionary--73iajoz#:~:text=To%20simply%20check%20if%20a,')%20%23%20Dogs%20found!&text=A%20dictionary%20can%20be%20a,counting%20the%20occurrence%20of%20items.
To simply check if a key exists in a Python dictionary you can use the in operator to search through the dictionary keys like this: pets = {'cats': 1, '...
_________
_________
Dictionary
https://www.programiz.com/python-programming/dictionary
In this tutorial, you'll learn everything about Python dictionaries; how they are created, accessing, adding, removing elements from them and various built-in methods.
_________
_________
Key index in Dictionary
https://www.geeksforgeeks.org/python-key-index-in-dictionary/
The concept of dictionary is similar to that of map data structure in C++ language, but with the exception that keys in dictionary has nothing to do with its ordering, …
_________
_________
String Formatting Best Practices
https://realpython.com/python-string-formatting/
Learn the four main approaches to string formatting in Python, as well as their strengths and weaknesses. You'll also get a simple rule of thumb for how to pick the bes …
_________
_________
Video Walk Through
https://www.youtube.com/watch?v=fo7hXynbkxI
In this video, you will learn how to solve these: 0:20 Are the Numbers Equal?, 2:08 Let's Fuel Up!, 4:31 Luke, I Am Your ...
_________
_________
f-strings
https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/?ref=gcse
The idea behind f-strings is to make string interpolation simpler. To create an f-string, prefix the string with the letter “ f ”. The string itself can be formatted i …
_________
_________
False Memory
https://en.wikipedia.org/wiki/False_memory
is a phenomenon where a person recalls something that did not happen or recalls it differently from the way it actually happened. Suggestibility, activation of associat …
_________
""" 
# Your code should go here:

def relation(str1):
    match str1.lower():
        case "darth vader" :
            return "Luke, I am your father."
        case "leia" :
            return "Luke, I am your sister."
        case "han" :
            return "Luke, I am your brother in law."
# Is there any more better way to solve this?

print(relation("Darth Vader"))
print(relation("Leia"))
print(relation("Han"))

# The program is complete.