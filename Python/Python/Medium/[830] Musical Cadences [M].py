"""
####  Musical Cadences  ####

In music, cadences act as punctuation in musical phrases, and help to mark the end of phrases. Cadences are the two chords at the end of a phrase. The different cadences are as follows:
___
*) V followed by I is a Perfect Cadence
*) IV followed by I is a Plagal Cadence
*) V followed by Any chord other than I is an Interrupted Cadence
*) Any chord followed by V is an Imperfect Cadence
___

Create a function where given a chord progression as a list, return the type of cadence the phrase ends on.


[Examples]

___
find_cadence(["I", "IV", "V"]) ➞ "imperfect"

find_cadence(["ii", "V", "I"]) ➞ "perfect"

find_cadence(["I", "IV", "I", "V", "vi"]) ➞ "interrupted"
_____



[Notes]

___
*) Return strings all in lowercase.
*) Only focus on the last two chords of a progression.
*) Return "no cadence" if none of the criteria match up.
*) I is a capital i, not a lowercase L.
___



[algorithms] [arrays] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
If ... Else
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics: Equals: a == b Not Equals: a != b Less than: a < b Less than or equal to: a <= b Greater than: a > b Gre …
_________
_________
Cadences
https://www.musictheoryacademy.com/how-to-read-sheet-music/cadences/
A cadence is a chord progression of at least 2 chords that ends a phrase or section of a piece of music. The easiest way to understand cadences in music is to think of …
_________

"""
#Your code should go here:

