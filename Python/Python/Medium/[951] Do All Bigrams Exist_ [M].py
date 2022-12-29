"""
####  Do All Bigrams Exist?  ####

You are given an input array of bigrams, and an array of words.
Write a function that returns True if every single bigram from this array can be found at least once in an array of words.


[Examples]

___
can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]) ➞ True

can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]) ➞ False
# "cu" does not exist in any of the words.

can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]) ➞ True

can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]) ➞ False
_____



[Notes]

___
*) A bigram is string of two consecutive characters in the same word.
*) If the list of words is empty, return False.
___



[higher_order_functions] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to Use Python
https://careerkarma.com/blog/python-any-and-all/
The Python any() and all() methods check if the values in a list evaluate to True. Learn how to use these methods on Career Karma.
_________
_________
What is bigram?
https://stackoverflow.com/questions/43463792/what-is-the-difference-between-bigram-and-unigram-text-features-extraction
n-gram is basically a set of occurring words within a given window so when n=1 it is Unigram. n=2 it is bigram. n=3 it is trigram, and so on. Now suppose a machine trie …
_________

"""
#Your code should go here:

