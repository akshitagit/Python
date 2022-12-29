"""
##Multi-division

Create a function, that will for a given a, b, c, do the following:
___
*) Add a to itself b times.
*) Check if the result is divisible by c.
___



[Examples]

___
abcmath(42, 5, 10) ➞ False
# 42+42 = 84,84+84 = 168,168+168 = 336,336+336 = 672, 672+672 = 1344
# 1344 is not divisible by 10

abcmath(5, 2, 1) ➞ True

abcmath(1, 2, 3) ➞ False
_____



[Notes]

___
*) "if the result is divisible by c", means that if you divide the result and c, you will get an integer (5, and not 4.5314).
*) The second test is correct.
___



[algebra] [loops] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
While Loops
https://www.w3schools.com/python/python_while_loops.asp
The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
_________
_________
Python Modulo Operator
https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/
The % symbol in Python is called the Modulo Operator. It returns the remainder of dividing the left hand operand by right hand operand. It's used to get the remainder o …
_________
_________
divmod() Method
https://www.w3schools.com/python/ref_func_divmod.asp
Get the reminder from a number divided by another.
_________
_________
Powers
https://brainly.in/question/17353500
The number of times a number is multiplied by itself is called​...
_________
_________
Asteriks
https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/#:~:text=Both%20*%20and%20**%20can%20be,calls%2C%20as%20of%20Python%203.5.&text=Functions%20in%20Python%20can't,an%20exception%20will%20be%20raised.
There are a lot of places you’ll see * and ** used in Python. These two operators can be a bit mysterious at times, both for brand new programmers and for folks moving …
_________
""" 
# Your code should go here:

