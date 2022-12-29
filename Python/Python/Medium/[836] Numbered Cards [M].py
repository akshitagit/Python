"""
####  Numbered Cards  ####

You have a pack of 5 randomly numbered cards, which can range from 0-9. You can win if you can produce a higher two-digit number from your cards, than your opponent. Return True if your cards win that round.


[Worked Example]

___
win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]) ➞ True
# Your cards can make the number 96
# Your opponent can make the number 73
# You win the round since 96 > 73
_____



[Examples]

___
win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]) ➞ True

win_round([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]) ➞ False

win_round([4, 3, 4, 4, 5], [3, 2, 5, 4, 1]) ➞ False
_____



[Notes]

Return False if you and your opponent reach the same maximum number (see example #3).


[arrays] [games] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to Compare Two Lists in Python
https://www.journaldev.com/37089/how-to-compare-two-lists-in-python
In this article, we will understand the different ways to compare two lists in Python. We often come across situations wherein we need to compare the values of the data …
_________
_________
sorted() Method
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________
_________
Indexing and Slicing for Lists, Tuples, Strings, and other Sequential Types
https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
List is arguably the most useful and ubiquitous type in Python. One of the reasons it’s so handy is Python slice notation. In short, slicing is a flexible tool to build …
_________

"""
#Your code should go here:

