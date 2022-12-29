"""
####  Lottery Ticket  ####

Given a lottery ticket (ticket), represented by a list of 2-value lists, create a function to find out if you've won the jackpot.
To do this, you must first count the "mini-wins" on your ticket. Each sublist has both a string and a number within it. If the character code of any of the characters in the string matches the number, you get a mini-win. Note you can only have one mini-win per sublist.
Once you have counted all of your mini-wins, compare that number to the other input provided (win). If your number of mini-wins is more than or equal to win, return Winner!. Else, return Loser!.


[Examples]

___
lottery([["YYW", 70], ["WXK", 65], ["RPDI", 88]], 2)
➞ "Loser!"

lottery([["KG", 80], ["NTBBVZ", 79], ["CI", 73], ["AGXMEE", 74], ["IU", 68], ["VOSP" , 84]], 1)
➞ "Winner!"

lottery([["ZSAMZB", 81], ["XWWCXP", 72], ["SYBRQOHP", 88], ["HJSVV", 75]], 1)
➞ "Loser!"
_____



[Notes]

___
*) All inputs will be in the correct format.
*) Strings on ticket are not always the same length.
___



[arrays] [language_fundamentals] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
chr() Function
https://www.w3schools.com/python/ref_func_chr.asp
Returns the character that represents the specified unicode.
_________
_________
ord() Function
https://favtutor.com/blogs/ord-function-python
Learn what is ord() function in python and how to use the ord() function with one character and multiple characters.
_________

"""
#Your code should go here:

