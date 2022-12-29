"""
##Calculating Damage

Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.


[Examples]

___
damage(40, 5, "second") ➞ 200

damage(100, 1, "minute") ➞ 6000

damage(2, 100, "hour") ➞ 720000
_____



[Notes]

Return "invalid" if damage or speed is negative.


[conditions] [math] 



-------------------------------------------------------------------
[Resources]
_________
Dictionary get() Method
https://www.w3schools.com/python/ref_dictionary_get.asp
Get method in python dictionary, doesn't throw error if, key is not in dictionary.
_________
_________
index() Method
https://www.programiz.com/python-programming/methods/string/index
Returns the index of a substring inside the string (if found). If the substring is not found, it raises an exception.
_________
_________
Dictionary
https://www.programiz.com/python-programming/dictionary
In this tutorial, you'll learn everything about Python dictionaries; how they are created, accessing, adding, removing elements from them and various built-in methods.
_________
""" 
# Your code should go here:

def damage(damage, speed, timeParameter):
    if damage < 0 or speed < 0:
        return "Invalid, speed or damage cannot be negative."
    else:
        match timeParameter:
            case "second" | "sec" | "secs" | "seconds":
                return damage * speed
            case "minute" | "min" | "mins" | "minutes":
                return (speed * 60) * damage
            case "hour" | "hours" | "hr" | "hrs":
                return (speed * (60 ** 2)) * damage

print(damage(40, 5, "seconds"))
print(damage(100, 1, "minutes"))
print(damage(2, 100, "hrs"))

# The program is complete.