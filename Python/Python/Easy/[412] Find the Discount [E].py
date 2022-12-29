"""
##Find the Discount

Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.



[Examples]

___
dis(1500, 50) ➞ 750

dis(89, 20) ➞ 71.2

dis(100, 75) ➞ 25
_____



[Notes]

Your answer should be rounded to two decimal places.


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
round() Function
https://www.programiz.com/python-programming/methods/built-in/round
Returns a floating-point number rounded to the specified number of decimals. In this tutorial, we will learn about Python round() in detail with the help of examples.
_________
_________
Discount Calculator
https://www.calculator.net/discount-calculator.html?pricebefore=700&discount=10&priceafter=&savedamount=&format=p&x=92&y=31
A percent off of a price typically refers to getting some percent, say 10%, off of the original price of the product or service. For example, if a good costs $45, with …
_________
_________
Percentages, Mathematics, and GCSE Revision
https://revisionmaths.com/gcse-maths-revision/number/percentages
Percentages GCSE Maths revision section of Revision Maths, including: definitions, examples and videos.
_________
""" 
# Your code should go here:

def disPrice(ogPrice, discPerc):
    return round((ogPrice * (1 -( discPerc/100))),2)

print(disPrice(1500, 50))
print(disPrice(89, 20))
print(disPrice(100, 75))

# The program is complete.