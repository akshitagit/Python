"""
####  Virtual DAC  ####

In electronics, a digital-to-analog converter (DAC, D/A, or D-to-A) is a system that converts a binary representation of that signal into an analog output. An 8 bit converter can represent a maximum of 2^8 different values, with each successive value differing by 1/256 of the full scale value, this becomes the system resolution.
Create a function that takes a decimal number representation of a signal and returns the analog voltage level that would be created by a DAC if it were given the same number in binary.
While value range is 0-1023, reference range is 0-5.00 volts. Value and reference is directly proportional.
This DAC has 10 bits of resolution and the DAC reference is set at 5.00 volts.


[Examples]

___
V_DAC(0) ➞ 0

V_DAC(1023) ➞ 5

V_DAC(400) ➞ 1.96
_____



[Notes]

You should return your value rounded to two decimal places.


[functional_programming] 



-------------------------------------------------------------------
[Resources]
_________
Analog to Digital Conversion
https://learn.sparkfun.com/tutorials/analog-to-digital-conversion/relating-adc-value-to-voltage
The ADC reports a ratiometric value. This means that the ADC assumes 5V is 1023 and anything less than 5V will be a ratio between 5V and 1023.
_________
_________
Directly Proportional and Inversely Proportional
https://www.mathsisfun.com/algebra/directly-inversely-proportional.html
Directly proportional: as one amount increases another amount increases at the same rate. Inversely Proportional: when one value decreases at the same rate that the oth …
_________
_________
Direct & Inverse Proportions
https://www.onlinemathlearning.com/proportions.html
The following diagram gives the steps to solve ratios and direct proportion word problems. Scroll down the page for examples and step-by-step solutions.
_________

"""
#Your code should go here:

