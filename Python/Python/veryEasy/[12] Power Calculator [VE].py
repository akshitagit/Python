"""
##Power Calculator

Create a function that takes voltage and current and returns the calculated power.


[Examples]

___
circuit_power(230, 10) ➞ 2300

circuit_power(110, 3) ➞ 330

circuit_power(480, 20) ➞ 9600
_____



[Notes]

Requires basic calculation of electrical circuits (see Resources for info).


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Ohms Law and Power
https://www.electronics-tutorials.ws/dccircuits/dcp_2.html
By knowing any two values of the Voltage, Current or Resistance quantities we can use Ohms Law to find the third missing value. Ohms Law is used extensively in electron …
_________
_________
Basic Operators
https://www.google.com.au/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiOtqHg5YTsAhXJzTgGHeQuDWMQFjABegQIARAB&url=https%3A%2F%2Fwww.learnpython.org%2Fen%2FBasic_Operators&usg=AOvVaw3Iu6i7v6B9kV-Y7EYIObQy
This section explains how to use basic operators in Python. Arithmetic Operators Just as any other programming languages, the addition, subtraction, multiplication, an …
_________
_________
Power and Energy Formula
https://electronicsclub.info/power.htm#:~:text=To%20calculate%20power%2C%20P%3A%20put,the%20equation%20is%20I%20%3D%20P%2F&text=To%20calculate%20voltage%2C%20V%3A%20put,the%20equation%20is%20V%20%3D%20P%2F
Power is the rate of using or supplying energy. Power is measured in watts (W). Energy is measured in joules (J). Time is measured in seconds (s).
_________
""" 
# Your code should go here:

def circuitPower(voltage, current):
    return (voltage * current)

print(circuitPower(230,10))
print(circuitPower(110,3))
print(circuitPower(480,20))

# The program is complete.