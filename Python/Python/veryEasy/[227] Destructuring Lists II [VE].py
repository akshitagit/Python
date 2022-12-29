"""
##Destructuring Lists II

We can destructure lists like this:
___
arr = ["1", "2", "3"]
a, b, c = arr
_____

but what if the list has nested lists, like the following?
___
arr = ["cars", "planes", ["trains", ["motorcycles"]]]

trans1 = arr[0]
trans2 = arr[1]
trans3 = arr[2][0]
trans4 = arr[2][1][0]

println(trans1) # outputs "cars"
println(trans2) # outputs "planes"
println(trans3) # outputs "trains"
println(trans4) # outputs "motorcycles"
_____

Can you use list destructuring to assign all four variables at once?


[Notes]

Check the Resources tab for more examples.


[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
4 Powerful Python Destructuring Features
https://towardsdatascience.com/4-powerful-python-destructuring-features-7128aa2bc400
Destructuring assignments are a shorthand syntax for mapping one or more variables from the left-hand side to the right-hand side counterparts. It’s handy in unpacking …
_________
_________
Destructuring in Python
https://blog.tecladocode.com/destructuring-in-python/
In this week's post we're going to look at a very interesting and versatile tool called destructuring. Destructuring (also called unpacking) is where we take a collecti …
_________
_________
Destructuring a List in Python like JavaScript
https://medium.com/@umaramanat66/destructuring-list-in-python-like-javascript-f7d4c0968538
Destructuring also referred to as unpacking in Python’s jargon . If you see code of pro-python developer you will see unpacking or destructing of list, dictionary. This …
_________
""" 
# Your code should go here:

