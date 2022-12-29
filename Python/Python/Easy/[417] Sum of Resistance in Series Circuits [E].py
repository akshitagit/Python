"""
##Sum of Resistance in Series Circuits

When resistors are connected together in series, the same current passes through each resistor in the chain and the total resistance,
RT, of the circuit must be equal to the sum of all the individual resistors added together. That is:
___
RT = R1 + R2 + R3 ...
_____

Create a function that takes an array of values resistance that are connected in series,
and calculates the total resistance of the circuit in ohms.
The ohm is the standard unit of electrical resistance in the International System of Units ( SI ).


[Examples]

___
series_resistance([1, 5, 6, 3]) ➞ "15 ohms"

series_resistance([16, 3.5, 6]) ➞ "25.5 ohms"

series_resistance([0.5, 0.5]) ➞ "1.0 ohm"
_____



[Notes]

___
*) All inputs will be valid.
*) Notice the singular ohm for values <= 1.
*) This challenge was inspired by Joshua Señoron's Python Sum of Resistance in Parallel Circuits challenge. You can find it here.
___



[arrays] [loops] [math] [physics] 



-------------------------------------------------------------------
[Resources]
_________
sum() Method
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
A Guide to the Newer Python String Format Techniques
https://realpython.com/python-formatted-output/
In the last tutorial in this series, you learned how to format string data using the string modulo operator. In this tutorial, you'll see two more items to add to your …
_________
_________
format() Function
https://www.educba.com/python-format-function/
Python has acquired a wide and peak level in the market like no language has done ever before, especially in the domain of Artificial Intelligence and Data Science. Kno …
_________
_________
If Else
https://pythonexamples.org/python-if-else-example/
Is used to implement conditional execution where in if the condition evaluates to true, if-block statement(s) are executed and if the condition evaluates to false, else …
_________
""" 
# Your code should go here:

def totalSeriesResistance(list1):
    if sum(list1) <=1:
        return "{sum} ohm".format(sum=(sum(list1)))
    else:
        return "{sum} ohms".format(sum=(sum(list1)))

print(totalSeriesResistance([1, 5, 6, 3]))
print(totalSeriesResistance([16, 3.5, 6]))
print(totalSeriesResistance([0.5, 0.5]))

# The program is complete.