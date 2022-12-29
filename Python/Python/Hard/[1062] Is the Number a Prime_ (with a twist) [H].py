"""
####  Is the Number a Prime? (with a twist)  ####

Write a function that takes a number and returns True if it's a prime; False otherwise. The number can be 2^64-1 (2 to the power of 63, not XOR). With the standard technique it would be O(2^64-1), which is much too large for the 10 second time limit imposed by Edabit.



[Examples]

___
prime(7) ➞ True

prime(56963) ➞ True

prime(5151512515524) ➞ False
_____



[Notes]

A "prime" number is a number that can only be divided by itself and 1 (upon division the result is a whole number).


[math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
In mathematics, the sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.
_________
_________
Prime Number
https://en.wikipedia.org/wiki/Prime_number#:~:text=The%20first%2025%20prime%20numbers,sequence%20A000040%20in%20the%20OEIS).&text=as%20the%20product-,.,is%20called%20an%20odd%20prime.
A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime i …
_________
_________
Prime Numbers Chart and Calculator
https://www.mathsisfun.com/prime_numbers.html
A Prime Number is a whole number that cannot be made by multiplying other whole numbers (if we can make it by multiplying other whole numbers it is a Composite Number) …
_________
_________
Checking if a Number Is a Prime Number
https://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
I have written the following code, which should check if the entered number is a prime number or not, but there is an issue I couldn't get through...
_________
_________
Witness Numbers to Determine Primality
https://www.youtube.com/watch?v=_MscGSN5J6o&t=15s
How to use Miller-Rabin algorithm (useful for extremely large numbers).
_________
_________
Sieve of Atkin
https://en.wikipedia.org/wiki/Sieve_of_Atkin
Is a modern algorithm for finding all prime numbers up to a specified integer. Compared with the ancient sieve of Eratosthenes, which marks off multiples of primes, t …
_________

"""
#Your code should go here:

