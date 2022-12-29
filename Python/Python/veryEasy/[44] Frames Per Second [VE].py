"""
##Frames Per Second

Create a function that returns the number of frames shown in a given number of minutes for a certain FPS.


[Examples]

___
frames(1, 1) ➞ 60

frames(10, 1) ➞ 600

frames(10, 25) ➞ 15000
_____



[Notes]

FPS stands for "frames per second" and it's the number of frames a computer screen shows every second.


[algorithms] [language_fundamentals] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
FPS (Frames Per Second) Definition
https://techterms.com/definition/fps
FPS is used to measure frame rate – the number of consecutive full-screen images that are displayed each second. It is a common specification used in video capture and …
_________
_________
Lambda Functions
https://realpython.com/python-lambda/
Python and other languages like Java, C#, and even C++ have had lambda functions added to their syntax, whereas languages like LISP or the ML family of languages, Haske …
_________
""" 
# Your code should go here:

def frames(secs, Fmulti):
    return (secs * (Fmulti * 60))

print(frames(1, 1))
print(frames(10, 1))
print(frames(10, 25))

# The program is complete.