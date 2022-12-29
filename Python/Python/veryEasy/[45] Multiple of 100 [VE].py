"""
##Multiple of 100

Create a function that takes an integer and returns True if it's divisible by 100, otherwise return False.


[Examples]

___
divisible(1) ➞ False

divisible(1000) ➞ True

divisible(100) ➞ True
_____



[Notes]

___
*) Don't forget to return the result.
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[algebra] [conditions] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
is_integer
https://docs.python.org/3/library/stdtypes.html#float.is_integer
Returns True if the floating number is whole, and false if it's a decimal number. (If a number can be cleanly divided by another, this will return True on that operation)
_________
_________
How do you check whether a number is divisible by another number?
https://stackoverflow.com/questions/8002217/how-do-you-check-whether-a-number-is-divisible-by-another-number-python
I need to test whether each number from 1 to 1000 is a multiple of 3 or a multiple of 5. The way I thought I'd do this would be to divide the number by 3, and if the re …
_________
_________
Syntax for an If Statement Using a Boolean
https://stackoverflow.com/questions/38423360/syntax-for-an-if-statement-using-a-boolean
Hey guys i just recently joined the python3 HypeTrain! However i just wondered how you can use an if statement onto a boolean: Example: RandomBool = True #and now how c …
_________
_________
Divisibility by 9 with Negative Number
https://math.stackexchange.com/questions/1288810/divisibility-by-9-with-negative-number
Multiplying by -1 doesn't change anything. If we have 18, which we know is divisible by 9, we just multiply it by -1 to get -18 and then we do the same to how many time …
_________
_________
Is 0 considered divisible by any integer?
https://gmatclub.com/forum/is-0-considered-divisible-by-any-integer-for-example-is-69240.html
Yes, zero is divisible by every integer, with one exception: nothing is divisible by zero. Zero divided by three is, of course, zero, which is an integer; therefore zer …
_________
""" 
# Your code should go here:

def div100(num1):
    if (num1 % 100 == 0):
        return True
    else:
        return False

print(div100(100))
print(div100(1000))
print(div100(100000))
print(div100(1))
print(div100(23))

# The program is complete.