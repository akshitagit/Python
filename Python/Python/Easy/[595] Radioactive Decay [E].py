"""
##Radioactive Decay

A half life is the amount of time for half of a radioactive substance to decay.
___
*) After 1 half life, 50% of a substance will be left.
*) After 2 half lives, 25% of a substance will be left.
*) After 3 half lives, 12.5% of a substance will be left, etc...
___

Create a function which calculates the remaining mass and the number of years that it took for the substance to decay. You will be given:
___
*) The mass of the substance.
*) The time in years for a halflife to elapse.
*) The number of half lives.
___



[Worked Example]

___
halflife_calculator(1000, 5730, 2) ➞ [250, 11460]

# There are 2 half lives, so the mass decays from 1000 to 500, then from 500 to 250.
# Each halflife is 5730 years, and since there were 2, it took 11460 years in total.
_____



[Examples]

___
halflife_calculator(1600, 6, 3) ➞ [200, 18]

halflife_calculator(13, 500, 1) ➞ [6.5, 500]

halflife_calculator(100, 35, 5) ➞ [3.125, 175]
_____



[Notes]

___
*) Round the final mass to three decimal places.
*) All inputs are positive numbers.
*) Return the final mass first, then the number of years.
___



[math] [physics] 



-------------------------------------------------------------------
[Resources]
_________
Half-Lives and Radioactive Decay Kinetics
https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Nuclear_Chemistry/Nuclear_Kinetics/Half-Lives_and_Radioactive_Decay_Kinetics
The half-life of a first-order reaction under a given set of reaction conditions is a constant. This is not true for zeroth- and second-order reactions. The half-life o …
_________
_________
pow() Function
https://www.w3schools.com/python/ref_func_pow.asp
Returns the value of x to the power of y (xy). If a third parameter is present, it returns x to the power of y, modulus z.
_________
_________
round() Function
https://www.w3schools.com/python/ref_func_round.asp
Round a number to only two decimals.
_________
""" 
# Your code should go here:

