"""
####  Malthusian Catastrophe  ####

A man named Thomas Malthus described what is now called a Malthusian Catastrophe. According to him, food production grows by a fixed amount, but population grows by a percentage. So, the food supply would soon be insufficient for the population.
Your job is to find out when that will occur. For this challenge, assume 1 population needs 1 unit of food production. Food production and population both start at 100. The year starts at 0.
The catastrophe happens when the population is larger than food production.
The function will pass:
___
*) food_growth ⁠— an integer ⁠— food production increase per year.
*) pop_mult ⁠— a floating-point number ⁠— population growth multiplier per year.
___



[Examples]

___
malthusian(4255, 1.41) ➞ 20
# { food_prod: 85,200, pop: 96,467.77..., year: 20 }

malthusian(9433, 1.09) ➞ 107
# { food_prod: 1,009,431, pop: 1,010,730.28..., year: 107 }

malthusian(5879, 1.77) ➞ 12
# { food_prod: 70,648, pop: 94,553.84..., year: 12 }
_____



[Notes]

___
*) Return the year that the overtake happens, not the next year.
*) Make sure you don't make the mistake of adding a year, then calculating the changes to food and population. That way, you miss year 0.
*) If the population and food production are equal, that is not a catastrophe.
___



[conditions] [dates] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Functions Creating Iterators for Efficient Looping
https://docs.python.org/3/library/itertools.html
This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
_________
_________
What is a Malthusian Catastrophe?
https://www.scienceabc.com/humans/malthusian-catastrophe.html
Malthus was of the opinion that the growth of human population is geometric (he estimated it to be doubling every 25 years) but food production would grow arithmetically
_________
_________
Definition of Multiplier
https://www.mathsisfun.com/definitions/multiplier.html
The number that you are multiplying by. But because we can multiply the two numbers in any order, it is better to use the word "factor". Try dragging the numerals to t …
_________
_________
Exponential Growth and Decay
https://www.mathsisfun.com/algebra/exponential-growth.html
Somethings always grows in relation to its current value, such as always doubling. Example: if a population of rabbits doubles every month we would have 2, then 4, then …
_________

"""
#Your code should go here:

