"""
##Destructuring Lists III

You can assign variables from lists with destructuring like this:
___
arr = ["eyes", "nose", "lips", "ears"]
eyes, nose, lips, ears = arr
_____

If you don't need every list index stored in a named variable, you can use _ as a throwaway variable.
___
arr = ["eyes", "nose", "lips", "ears"]
_ , nose, _, _ = arr
_____

... this assigns the value in arr[1] to the variable nose. The values in each other index will be assigned to the variable _
in order, overwriting each previous value. nose now holds the string "nose", and _ now holds the string "ears".
Use destructuring assignment on the given list to assign the string "lips" to the variable provided.
Do not use list indexing, or assigning variable names to any of the other strings.


[Notes]

Check the Resources tab for more examples.


[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Destructuring
https://www.codeproject.com/Articles/5270746/Python-Tuples-Lists-Destructuring-and-Loops
Python offers lists and tuples as data structures for collections. This module talks about these and how you can use them with destructuring and loops.
_________
_________
Destructuring Assignment
https://riptutorial.com/python/example/14981/destructuring-assignment
In assignments, you can split an Iterable into values using the "unpacking" syntax.
_________
_________
List Destructuring
http://www.phyast.pitt.edu/~micheles/scheme/scheme15.html
In my Adventures I have referred many times to pattern matching, but only in the context of compile time pattern matching in macros. There is another form of pattern ma …
_________
""" 
# Your code should go here:

arr = ["eyes", "nose", "lips", "ears"]
eyes1, nose1, lips1, ears1 = arr

print(eyes1)
print(nose1)
print(lips1)
print(ears1)

# The program is complete.