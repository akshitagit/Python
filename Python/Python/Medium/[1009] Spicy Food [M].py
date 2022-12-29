"""
####  Spicy Food  ####

The facts are:

Given your friend's unfortunate taste preferences, you decide to split the bill only for non-spicy items. You will pay in full for the spicy dishes.
Given two ordered lists, one classifying the dishes as spicy vs. non-spicy and the other listing their prices, write a function that outputs a list where the first element is how much you pay and the second element is how much your friend pays.
___
bill_split(["S", "N", "S", "S"], [13, 18, 15, 4]) ➞ [41, 9]

# Since:
# You pay: [13, 9, 15, 4] = 41
# Friend pays: [0, 9, 0, 0] = 9
_____



[Examples]

___
bill_split(["N", "S", "N"], [10, 10, 20]) ➞ [25, 15]
# You pay for half of both "N" dishes (5 + 10) and entirely pay for the "S" dish (10).

bill_split(["N", "N"], [10, 10]) ➞ [10, 10]

bill_split(["S", "N"], [41, 10]) ➞ [46, 5]
_____



[Notes]

___
*) The dishes are in the same order for both input lists.
*) Remember to output a list in this order: [your payment, friend's payment]
*) The list will contain at least one non-spicy dish N (you're not going to let your poor friend go hungry, are you?).
*) Express both payments as integers.
___



[arrays] [higher_order_functions] 



-------------------------------------------------------------------
[Resources]
_________
zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
Creates an iterator that will aggregate elements from two or more iterables. You can use the resulting iterator to quickly and consistently solve common programming pro …
_________
_________
Unpack a Tuple
https://note.nkmk.me/en/python-tuple-list-unpack/
Elements of tuples and lists can be assigned to multiple variables. It is called sequence unpacking.
_________
_________
How to convert two lists into a dictionary?
https://stackoverflow.com/questions/209840/convert-two-lists-into-a-dictionary
Imagine that you have: keys = ['name', 'age', 'food'] values = ['Monty', 42, 'spam'] What is the simplest way to produce the following dictionary? a_dict = {'name' : …
_________
_________
How to use a for range loop to iterate through two lists?
https://stackoverflow.com/questions/54545751/how-to-use-a-for-range-loop-to-iterate-through-two-lists-in-python
Say I have one list consisting of either "W' or a 'L's meaning a game won or game lost, and a second list with integers representing points scored (and the positions co …
_________

"""
#Your code should go here:

