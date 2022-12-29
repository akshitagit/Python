"""
####  Mahjong Tiles  ####

Your goal is to create a function that returns a list with a string for each of the 108 tiles in the following format:
___
"rank suit"
_____

Where rank is a number from 1 to 9 and suit is one of the three suits (tong, tiao, wan), both written in the pinyin transcription of Mandarin Chinese (for numbers see table below).

Three of the tiles have special names. Each of the 4 copies of these tiles should be represented by their names only (no suit, no rank):
___
*) One of tong is called bing gan (饼干, cookie)
*) Two of tong is called yan jing (眼镜, glasses)
*) One of tiao is called ji (鸡, chicken)
___



[Examples of tiles]

___
Five of tong ➞ "wu tong"

Seven of wan ➞ "qi wan"

One of tiao ➞ "ji"

Three of tiao ➞ "san tiao"
_____



[Notes]

___
*) Don't forget to include 4 copies of each tile.
*) Don't forget to substitute the tiles with special names.
*) You can return the tiles in any order.
___



[arrays] [games] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Mahjong Tiles
https://en.wikipedia.org/wiki/Mahjong_tiles
Tiles of Chinese origin that are used to play mahjong as well as mahjong solitaire and other games. Although they are most commonly tiles, they may refer to playing ca …
_________
_________
Mahjong
https://en.wikipedia.org/wiki/Mahjong
A tile-based game that was developed in China during the Qing dynasty and has spread throughout the world since the early 20th century. It is commonly played by four pl …
_________
_________
itertools.product() Method
https://docs.python.org/3/library/itertools.html#itertools.product
Can take the cartesian product of two input variables.
_________

"""
#Your code should go here:

