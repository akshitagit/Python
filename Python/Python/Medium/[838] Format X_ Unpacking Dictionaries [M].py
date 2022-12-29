"""
####  Format X: Unpacking Dictionaries  ####

For each challenge of this series you do not need to submit a function. Instead, you need to submit a template string that can formatted in order to get a certain outcome.
Write three dictionaries and a template string according to the following example. Notice the article "a" in the third example:


[Example]

___
dic1 = {"yourkeys": "yourvalues"}
dic2 = {"yourkeys": "yourvalues"}
dic3 = {"yourkeys": "yourvalues"}
template = "yourtemplatestringhere"

template.format(**dic1) ➞ "I like Mary, I don't like May."
template.format(**dic2) ➞ "I love Eda, I don't love Bit."
template.format(**dic3) ➞ "I have a Pidgey, I don't have a Rattata."
_____



[Tips]

The elements of a dictionary can be unpacked and passed to .format() as keyword arguments using a double star operator **:
___
product = {"name": "pokeball", "price": 20}
"One {name} is ${price:.2f}".format(**product) ➞ "One pokeball is $20.00"
_____



[Notes]

___
*) Submit a string, not a function.
*) Do not change the names of the variables template, dic1, dic2 and dic3.
*) You can find all the exercises in this series over here.
___



[formatting] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String Formatting with str.format() in Python
https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
This tutorial will guide you through some of the common uses of string formatters in Python, which can help make your code and program more readable and user friendly.
_________
_________
format() Method
https://www.programiz.com/python-programming/methods/string/format
Formats the given string into a nicer output in Python.
_________
_________
*args and **kwargs
https://www.geeksforgeeks.org/args-kwargs-python/
We can pass a variable number of arguments to a function using special symbols.
_________

"""
#Your code should go here:

