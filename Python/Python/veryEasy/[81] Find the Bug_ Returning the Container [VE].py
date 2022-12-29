"""
##Find the Bug: Returning the Container

The packaging system is running wild! The candy is lying loose all over in the warehouse, the cereal is missing,
and bread is stuffed in a bottle. What is going on here? The candy should be in plastic and the bread should be in a bag.
The packaging machine is running the get_container() function to retrieve the container of a product. But something is not right...


[Examples]

___
get_container("Bread") ➞ "bag"

get_container("Beer") ➞ "bottle"

get_container("Candy") ➞ "plastic"

get_container("Cheese") ➞ None
_____



[Notes]

Think about what the object's packaging should be.


[bugs] [conditions] [control_flow] [logic] 



-------------------------------------------------------------------
[Resources]
_________
How to access elements from a dictionary?
https://www.programiz.com/python-programming/dictionary#access
While indexing is used with other container types to access values, dictionary uses keys. Key can be used either inside square brackets or with the get() method. The di …
_________
_________
Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp
Is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
_________
_________
Convert Key-Value Pair Comma Separated String into Dictionary
https://www.geeksforgeeks.org/python-convert-key-value-pair-comma-separated-string-into-dictionary/
Given a string, with different key-value pairs separated with commas, the task is to convert that string into the dictionary. These types of problems are common in web …
_________
""" 
# Your code should go here:

def getContainer(product):
    input1 = product[0].upper() + product[1:].lower()
    container = {
        "Bread" : "bag",
        "Beer" : "bootle",
        "Candy" : "plastic"
    }
    if input1 in container:
        return container[input1]
    else:
        return None

print(getContainer("bread"))
print(getContainer("Beer"))
print(getContainer("beer"))
print(getContainer("Candy"))

print(getContainer("Cheese"))
print("\nJust checking the type of Non dict element:- ")
print(type(getContainer("Cheese")))

# The program is complete.