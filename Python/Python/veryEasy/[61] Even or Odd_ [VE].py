"""
##Even or Odd?

Given a list of integers, determine whether the sum of its elements is even or odd.
The return value should be a string ("odd" or "even").
If the input list is empty, consider it as a list with a zero ([0]).


[Examples]

___
even_or_odd([0]) ➞ "even"

even_or_odd([1]) ➞ "odd"

even_or_odd([]) ➞ "even"

even_or_odd([0, 1, 5]) ➞ "even"
_____



[Notes]

N/A


[algorithms] [arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
What Does the % Symbol Mean in Python?
https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/#:~:text=The%20%25%20symbol%20in%20Python%20is,remainder%20of%20a%20division%20problem.&text=In%20the%20previous%20example%20a,and%20the%20remainder%20is%20returned.
When you see the % symbol, you may think "percent". But in Python, as well as most other programming languages, it means something different.
_________
_________
Print Even Numbers in a List
https://www.geeksforgeeks.org/python-program-to-print-even-numbers-in-a-list/
Given a list of numbers, write a Python program to print all even numbers in the given list.
_________
""" 
# Your code should go here:

def sumListInt(list1):
    sum = 0
    for i in list1:
        sum += i
    if sum % 2 == 0:
        return "even"
    else:
        return "odd"

print(sumListInt([0]))
print(sumListInt([1]))
print(sumListInt([]))
print(sumListInt([0, 1, 5]))

# The program is complete.