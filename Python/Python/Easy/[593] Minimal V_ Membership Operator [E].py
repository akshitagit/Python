"""
##Minimal V: Membership Operator

Check the principles of minimalist code in the intro to the first challenge.
In the Code tab you will find a code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section below.
Write a function that returns the boolean True if the given two lists do not share any numbers, and False otherwise.


[Tips]

The operators in and not in test for membership. x in s evaluates to True if x is a member of s, and False otherwise.
For example, the code:
___
def startswithvowel(word):
    for vowel in "aeiou":
        if word[0] == vowel:
            return True
    return False
_____

Can be simplified to:
___
def startswithvowel(word):
    return word[0] in "aeiou"
_____



[Bonus]

Here are more examples:
___
12 in [1, 50, 12, 43, 7] ➞ True
1 in [12, 111111, "x"] ➞ False
[3, 4] in [1, 2, 3, 4, 5] ➞ False
3 in (True, 3, ["odd", "even"]) ➞ True
"odd" in (True, 3, ["odd", "even"]) ➞ False
"hello" in "hellomyfriend" ➞ True

"myfriend" not in "hello my friend" ➞ True
"bye" not in "bye my friend" ➞ False
2 not in {0: "even", 1: "odd"} ➞ True
1 not in {0: "even", 1: "odd"} ➞ False
_____



[Notes]

___
*) This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your suggestions in the Comments.
*) Readability is indeed a subjective concept. Let's discuss it! Feel free to leave your opinion in the Comments.
*) You can find all the exercises in this series over here.
___



[conditions] [language_fundamentals] [logic] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Python Membership and Identity Operators
https://www.geeksforgeeks.org/python-membership-identity-operators-not-not/
Membership operators are operators used to validate the membership of a value. It test for membership in a sequence, such as strings, lists, or tuples.
_________
_________
all() Method
https://www.programiz.com/python-programming/methods/built-in/all
Returns True when all elements in the given iterable are true. If not, it returns False.
_________
_________
Sets
https://www.w3schools.com/python/python_sets.asp
Is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
_________
_________
Python Membership Operators Example
https://www.tutorialspoint.com/python/membership_operators_example.htm
Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples. There are two membership operators as explained below ...
_________
_________
Membership Test Operations
https://docs.python.org/3/reference/expressions.html#membership-test-operations
The operators in and not in test for membership. x in s evaluates to True if x is a member of s, and False otherwise. x not in s returns the negation of x in s. All bui …
_________
""" 
# Your code should go here:

