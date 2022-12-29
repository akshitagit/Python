"""
####  Back and Forth  ####

In a board game, a player may pick up a card with several left or right facing arrows, with the number of arrows indicating the number of tiles to move. The player should move either left or right, depending on the arrow's direction.
Given a list of the arrows contained on a player's cards, return a singular string of arrowheads that are equivalent to all of the arrowheads.


[Worked Example]

___
calculate_arrowhead([">>", "<<", "<<<"]) ➞ "<<<"

# >> means to move 2 places right
# << means to move 2 places left (cancelling out >>)
# <<< means to move a further 3 places left
# overall, the movement can be written as <<<
_____



[Examples]

___
calculate_arrowhead([">>>>", "<", "<", "<"]) ➞ ">"

calculate_arrowhead([">", "<", ">>", "<", "<<<"]) ➞ "<<"

calculate_arrowhead([">>>", "<<<"]) ➞ ""
_____



[Notes]

Return an empty string if all the arrowheads cancel out.


[algorithms] [arrays] [strings] 



-------------------------------------------------------------------
[Resources]
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
count() Method
https://www.w3schools.com/python/ref_list_count.asp
Returns the number of elements with the specified value.
_________
_________
join() Function
https://www.google.ca/amp/s/www.geeksforgeeks.org/join-function-python/amp/
Is a string method and returns a string in which the elements of sequence have been joined by str separator.
_________

"""
#Your code should go here:

