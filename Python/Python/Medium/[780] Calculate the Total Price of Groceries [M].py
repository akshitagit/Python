"""
####  Calculate the Total Price of Groceries  ####

Create a function that takes a list of dictionaries (groceries) which calculates the total price and returns it as a number. A grocery dictionary has a product, a quantity and a price, for example:
___
{
  "product": "Milk",
  "quantity": 1,
  "price": 1.50
}
_____



[Examples]

___
# 1 bottle of milk:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 }
]) ➞ 1.5

# 1 bottle of milk & 1 box of cereals:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Cereals", "quantity": 1, "price": 2.50 }
]) ➞ 4

# 3 bottles of milk:
get_total_price([
  { "product": "Milk", "quantity": 3, "price": 1.50 }
]) ➞ 4.5

# Several groceries:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Eggs", "quantity": 12, "price": 0.10 },
  { "product": "Bread", "quantity": 2, "price": 1.60 },
  { "product": "Cheese", "quantity": 1, "price": 4.50 }
]) ➞ 10.4

# Some cheap candy:
get_total_price([
  { "product": "Chocolate", "quantity": 1, "price": 0.10 },
  { "product": "Lollipop", "quantity": 1, "price": 0.20 }
]) ➞ 0.3
_____



[Notes]

There might be a floating point precision problem in here...


[arrays] [logic] [math] [objects] 



-------------------------------------------------------------------
[Resources]
_________
round() Method
https://www.programiz.com/python-programming/methods/built-in/round
Returns the floating point number rounded off to the given ndigits digits after the decimal point. If no ndigits is provided, it rounds off the number to the nearest in …
_________
_________
Python Dictionaries
https://developer.rhino3d.com/guides/rhinopython/python-dictionaries/
One of the nice features of scripting languages such as Python is what is called an associative array. An associative array differs from a “normal” array in one major r …
_________
_________
get() Method
https://www.tutorialspoint.com/python/dictionary_get.htm
Returns a value for the given key. If key is not available then returns default value None.
_________

"""
#Your code should go here:

