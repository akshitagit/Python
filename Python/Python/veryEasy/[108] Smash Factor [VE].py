"""
##Smash Factor

Smash factor is a term in golf that relates to the amount of energy transferred from the club head to the golf ball.
The formula for calculating smash factor is ball speed divided by club speed.
Create a function that takes ball speed bs and club speed cs as arguments and returns the smash factor to the nearest hundredth.


[Examples]

___
smash_factor(139.4, 93.8) ➞ 1.49

smash_factor(181.2, 124.5) ➞ 1.46

smash_factor(154.7, 104.3) ➞ 1.48
_____



[Notes]

___
*) Remember to round to the nearest hundredth.
*) All values will be valid (so no dividing by zero).
___



[language_fundamentals] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Python round()
https://www.programiz.com/python-programming/methods/built-in/round
Returns a floating-point number rounded to the specified number of decimals. Learn about Python round() in detail with the help of examples.
_________
""" 
# Your code should go here:

def smashFactor(bs, cs):
    return round(bs/cs, 2)

print(smashFactor(139.4, 93.8))
print(smashFactor(181.2, 124.5))
print(smashFactor(154.7, 104.3))

# The program is complete.