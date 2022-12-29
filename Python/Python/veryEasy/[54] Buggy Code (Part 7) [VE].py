"""
##Buggy Code (Part 7)

Mubashir wants to swap two given numbers!
It is not returning the right values. Can you help him fix it?
___
a = 100
b = 200
a, b = swap(a, b)
print(a, b) # Should print out "200, 100", but the function prints out "100, 100"
_____



[Examples]

___
swap(100, 200) ➞ [200, 100]

swap(44, 33) ➞ [33, 44]

swap(21, 12) ➞ [12, 21]
_____



[Notes]

N/A


[bugs] [interview] [language_fundamentals] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Swap Two Variables
https://www.programiz.com/python-programming/examples/swap-variables
In this example, you will learn to swap two variables by using a temporary variable and, without using temporary variable.
_________
_________
Swap Two Variables Using XOR
https://betterexplained.com/articles/swap-two-variables-using-xor/
Most people would swap two variables x and y using a temporary variable, like this...
_________
""" 
# Your code should go here:

def swap(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2

def swap1(num1, num2):
    num1, num2 = num2, num1 # Python explicit method of swapping.
    return num1, num2

def swap2(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return num1, num2

def swap3(num1, num2):
    num1 = num1 * num2
    num2 = num1 / num2
    num1 = num1 / num2
    return int(num1), int(num2)

print("swap function: ")
print(swap(100, 200))
print(swap(44, 33))
print(swap(21, 12))

print("\nswap1 function:")
print(swap1(100, 200))
print(swap1(44, 33))
print(swap1(21, 12))

print("\nswap2 function:")
print(swap2(100, 200))
print(swap2(44, 33))
print(swap2(21, 12))

print("\nswap3 function:")
print(swap3(100, 200))
print(swap3(44, 33))
print(swap3(21, 12))

# The program is complete.

