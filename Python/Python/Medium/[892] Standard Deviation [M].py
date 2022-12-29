"""
####  Standard Deviation  ####

The central tendency measures (mean, mode and median) sometimes aren't enough descriptives in a data set analysis. For example, given two lists A=[15, 15, 15, 14, 16] and B=[2, 7, 14, 22, 30] the mean is μ=15 in both cases, however the values of second list are clearly more spread out from the average value. The standard deviation (also called sigma, the greek lowercase letter σ) measures the spread of the values in a data set and transform the "clearly more spread out than" assertion in a proofed statistical assertion. You can find more information in the Resources tab.
The standard deviation is calculated following five steps:

Given a list of values return the standard deviation rounded to the nearest hundredth.


[Examples]

___
standard_deviation([3, 5, 7]) ➞ 1.63
// |(3-5)|+|(5-5)|+|(7-5)| = 2² + 0 + 2² = 8 / 3 = square root of 2.66 = 1.63

standard_deviation([5, 5, 5]) ➞ 0
// Values aren't deviating from the mean.

standard_deviation([-3, -5, -7]) ➞ 1.63
// Remember: absolute differences!
_____



[Notes]

___
*) All given lists are valid, no exceptions to handle.
*) Lists can contain either positive or negative integers.
*) Remember to round to the nearest hundredth at the end.
___



[arrays] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Standard Deviation
https://en.wikipedia.org/wiki/Standard_deviation
In statistics, the standard deviation (SD, also represented by the lower case Greek letter sigma σ for the population standard deviation or the Latin letter s for the s …
_________
_________
round() Method
https://www.tutorialspoint.com/python/number_round.htm
Returns x rounded to n digits from the decimal point.
_________
_________
2 Ways to Calculate Standard Deviation in Python
https://honingds.com/blog/python-standard-deviation/
In this post, we will learn how to calculate standard deviation in Python. Standard deviation is the measure of dispersion of a set of data from its mean.
_________

"""
#Your code should go here:

