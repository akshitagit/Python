"""
####  Algorithms I: Introduction to Recursion  ####

Welcome to the beginning of this collection on Computer Science Algorithms. Admittedly there are other challenges on Edabit that deal with recursion and algorithmic processes, but these particular challenges are designed to give examples and to educate users on the topics being covered.


[Recursion]

In computer science, "recursion" is the act of writing a function that calls itself from within its own code. The function below better helps explain and illustrate recursion by simply counting down from a given number to zero:
___
def factorial(num):
    targetNumber = 0

  if num == targetNumber:
    print("Countdown complete!")
  else:
    factorial(num - 1)
_____



[Explanation]

The above function starts by initializing the target number, which is zero, then it creates a base case by checking if the inputted number has reached the target number yet. If it has, then the function ends and it prints the statement, else the function inputs num subtracted by one and then runs the function again.
When using recursive functions a "Base Case" is needed. A base case will stop the function once it reaches its intended goal. In the absence of a base case, the program can either crash due to "Stack Overflow" or by initiating an "Infinite Loop."
On a side note, initializing variables in recursive functions can sometimes be problematic because when the function runs again it will reset the value of that variable. For this specific recursive function the variable works fine because the target number we're trying to reach is consistently zero.


[Instructions]

The recursive function for this challenge should return the factorial of an inputted integer. If anyone needs a refresher, factorials in mathematics are represented by an exclamation point placed to the right of a number: 4! = 4 x 3 x 2 x 1 = 24


[Examples]

___
factorial(5) ➞ 120

factorial(3) ➞ 6

factorial(2) ➞ 2
_____



[Notes]

___
*) Print statements can be added to the Countdown function example for illustrative purposes if need be.
*) Terms that are placed in italics ("example"), while not always necessary to completing the challenge, can be helpful or just generally good to know as an aspiring programmer or computer science student/enthusiast.
*) Several of the challenges that will be covered in this collection on algorithms can be solved non-recursively and without implementing the algorithms described in each challenge. I implore anyone solving these challenges to do them as intended. Not understanding the concepts taught will be an obstacle to later challenges and won't aid anyone in advancing their skills as a programmer.
*) If you are stuck please check the Resources tab, Comments tab, or if you're really stuck, use the Solutions tab to unlock the answers.
___



[algorithms] [logic] [math] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
What is Recursion?
https://www.geeksforgeeks.org/recursion/
The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called as recursive function. Using recursive …
_________
_________
Infinite Loop
https://en.wikipedia.org/wiki/Infinite_loop
An infinite loop (or endless loop) is a sequence of instructions in a computer program which loops endlessly, either due to the loop having no terminating condition, ha …
_________
_________
Factorial
https://en.wikipedia.org/wiki/Factorial
In mathematics, the factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. The value of 0! is 1, according t …
_________
_________
Stack Overflow
https://en.wikipedia.org/wiki/Stack_overflow
In software, a stack overflow occurs if the call stack pointer exceeds the stack bound. The call stack may consist of a limited amount of address space, often determine …
_________

"""
#Your code should go here:

