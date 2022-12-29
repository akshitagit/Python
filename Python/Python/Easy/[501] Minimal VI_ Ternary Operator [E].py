"""
##Minimal VI: Ternary Operator

Check the principles of minimalist code in the intro to the first challenge.
In the Code tab you will find a code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section below.
Write a function that returns the strings:
___
*) "both" if both given booleans a and b are True.
*) "first" if only a is True.
*) "second" if only b is True .
*) "neither" if both a and b are False.
___



[Tips]

If-else statements can be written as a oneliner using Python's ternary operator.
For example, the code:
___
def startswith(name):
  if name[0] in "AEIOU":
    return "vowel"
  else:
    return "consonant"
_____

Can be simplified to:
___
def startswith(name):
  return "vowel" if name[0] in "AEIOU" else "consonant"
_____



[Bonus]

You can concatenate as many ternary operators as you want. However, concatenating too many will definitely diminish the readability of your code.
___
"majority" if  x > 50 else "minority" if x < 50 else "draw"
_____



[Notes]

___
*) This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your suggestions in the Comments.
*) Readability is indeed a subjective concept. Let's discuss it! Feel free to leave your opinion in the Comments.
*) You can find all the exercises in this series over here.
___



[conditions] [language_fundamentals] [logic] 



-------------------------------------------------------------------
[Resources]
_________
What is the ternary operator in Python?
https://www.educative.io/edpresso/what-is-the-ternary-operator-in-python
The ternary operator can be thought of as a simplified, one-line version of the if-else statement to test a condition.
_________
_________
Ternary Operator in Python
https://www.geeksforgeeks.org/ternary-operator-in-python/
Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in versio …
_________
_________
Ternary Operators
https://book.pythontips.com/en/latest/ternary_operators.html
Ternary operators are more commonly known as conditional expressions in Python. These operators evaluate something based on a condition being true or not. They became a …
_________
_________
Ternary Operator in Python
https://www.tutorialspoint.com/ternary-operator-in-python
The ternary operator in python is used to return a value based on the result of a binary condition. It takes binary value(condition) as an input, so it looks similar to …
_________
""" 
# Your code should go here:

