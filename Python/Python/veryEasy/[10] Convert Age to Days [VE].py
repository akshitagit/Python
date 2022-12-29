"""
##Convert Age to Days

Create a function that takes the age in years and returns the age in days.


[Examples]

___
calc_age(65) ➞ 23725

calc_age(0) ➞ 0

calc_age(20) ➞ 7300
_____



[Notes]

___
*) Use 365 days as the length of a year for this challenge.
*) Ignore leap years and days between last birthday and now.
*) Expect only positive integer inputs.
___



[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How to Convert Days to Age
https://www.youtube.com/watch?v=ZClu_I6U6aM
How to convert days to age.
_________
_________
How many days are in a year?
https://www.quora.com/How-many-days-are-in-a-year
How many days are in a year?
_________
_________
How to Calculate Age Manually?
http://99calculator.com/calculate-age-manually/#:~:text=First%20of%20all%2C%20the%20current,resultant%20value%20is%20the%20age.
The process of calculating age involves comparing one’s birth year with the year in which age needs to be calculated. First of all, the current ongoing year is taken no …
_________
_________
Multiplying and Dividing Numbers in Python 
https://www.pythoncentral.io/multiplying-dividing-numbers-python/
Use this handy beginner's tutorial to understand how to multiply and divide numbers in python using the appropriate operators.
_________
""" 
# Your code should go here:

def ageToDays(num1=int):
    if int(num1) >= 0:
        return int(num1) * 365
    else:
        return "Please input positive int for age."

print(ageToDays(65))
print(ageToDays(0))
print(ageToDays(20))
print(ageToDays("10"))
