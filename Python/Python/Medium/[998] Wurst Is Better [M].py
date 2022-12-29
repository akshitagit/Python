"""
####  Wurst Is Better  ####

Wurst is the best. Create a function that takes a string and replaces every mention of any type of sausage with the German word "Wurst," unless—of course—the sausage is already a type of German "Wurst" (i.e. "Bratwurst", see below), then leave the sausage name unchanged.



[Rules]

___
*) Append sausages from the "Convert to Wurst" column with "wurst".
*) Do not replace any German sausage with the word "Wurst".
*) The word "Wurst" must be title case.
___



[Examples]

___
wurst_is_better("I like chorizos, but not sausages") ➞ "I like Wursts, but not Wursts"

wurst_is_better("sich die Wurst vom Brot nehmen lassen") ➞ "sich die Wurst vom Brot nehmen lassen"

wurst_is_better("Bratwurst and Rostbratwurst are sausages") ➞ "Bratwurst and Rostbratwurst are Wursts"
_____



[Notes]

All German sausage names contain the word "wurst".


[regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
re.sub() function
https://www.codespeedy.com/re-sub-in-python/
Replaces the substrings that match with the search pattern with a string of user's choice.
_________
_________
join() Method
https://www.tutorialspoint.com/python/string_join.htm
Returns a string in which the string elements of sequence have been joined by str separator.
_________
_________
How to Use Split
http://www.pythonforbeginners.com/dictionary/python-split
At some point, you may need to break a large string down into smaller chunks, or strings. This is the opposite of concatenation which merges or combines strings into one.
_________
_________
Pattern Matching with Regular Expressions
https://automatetheboringstuff.com/chapter7/
You may be familiar with searching for text by pressing CTRL-F and typing in the words you’re looking for. Regular expressions go one step further: They allow you to sp …
_________

"""
#Your code should go here:

