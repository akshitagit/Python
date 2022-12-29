"""
##Sum of Resistance in Parallel Circuits

If two or more resistors are connected in parallel, the overall resistance of the circuit reduces. It is possible to calculate the total resistance of a parallel circuit by using this formula:

Create a function that takes a list of parallel resistance values, and calculates the total resistance of the circuit.


[Worked Example]

___
parallel_resistance([6, 3, 6]) ➞ 1.5

# 1/RTotal = 1/6 + 1/3 + 1/6
# 1/RTotal = 2/3
# RTotal = 3/2 = 1.5
_____



[Examples]

___
parallel_resistance([6, 3]) ➞ 2

parallel_resistance([10, 20, 10]) ➞ 4

parallel_resistance([500, 500, 500]) ➞ 166.6
# Round to the nearest decimal place
_____



[Notes]

___
*) Note that you should rearrange to return the RTotal, not 1 / RTotal.
*) Round to the nearest decimal place.
*) All inputs will be valid.
___



[arrays] [loops] [math] [physics] 



-------------------------------------------------------------------
[Resources]
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
round() Function
https://www.programiz.com/python-programming/methods/built-in/round
Returns a floating-point number rounded to the specified number of decimals. In this tutorial, we will learn about Python round() in detail with the help of examples.
_________
_________
Calculate the Total Resistance of a Circuit Given in a String
https://stackoverflow.com/questions/46629215/calculate-the-total-resistance-of-a-circuit-given-in-a-string
The idea behind the program is to start at the beginning of the list and calculate the resistance of the first three elements of the list, then to append them at the be …
_________
_________
Resistors in Parallel
https://www.electronics-tutorials.ws/resistor/res_4.html
Resistors are said to be connected together in parallel when both of their terminals are respectively connected to each terminal of the other resistor or resistors.
_________
""" 
# Your code should go here:

