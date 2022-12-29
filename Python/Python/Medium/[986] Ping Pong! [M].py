"""
####  Ping Pong!  ####

A game of table tennis almost always sounds like Ping! followed by Pong! Therefore, you know that Player 2 has won if you hear Pong! as the last sound (since Player 1 didn't return the ball back).
Given a list of Ping!, create a function that inserts Pong! in between each element. Also:
___
*) If win equals True, end the list with Pong!.
*) If win equals False, end with Ping! instead.
___



[Examples]

___
ping_pong(["Ping!"], True) ➞ ["Ping!", "Pong!"]

ping_pong(["Ping!", "Ping!"], False) ➞ ["Ping!", "Pong!", "Ping!"]

ping_pong(["Ping!", "Ping!", "Ping!"], True) ➞ ["Ping!", "Pong!", "Ping!", "Pong!", "Ping!", "Pong!"]
_____



[Notes]

___
*) You will always return the ball (i.e. the Pongs are yours).
*) Player 1 serves the ball and makes Ping!.
Return a list of strings.
___



[algorithms] [arrays] [games] 



-------------------------------------------------------------------
[Resources]
_________
len() Method
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
_________
List Multiplication and Common References
https://riptutorial.com/python/example/12259/list-multiplication-and-common-references
The reason is that [[]] * 3 doesn't create a list of 3 different lists. Rather, it creates a list holding 3 references to the same list object. As such, when we append …
_________
_________
Insert an Element Into a List
https://www.w3schools.com/python/python_lists_add.asp
Different methods to add list items.
_________

"""
#Your code should go here:

