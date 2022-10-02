#!/usr/bin/python3
# Sat 1 Oct 2022
# Authored by: Mohammad Javad Nikbakht <javadnikbakht@mail.com>

# Python3 code to count vowel in a string using set python data type
  
def vowel_count(given_str: str): 
      
    count = 0
      
    # Creating a set of vowels in English Language 
    vowel = set("aeiouAEIOU") 
      
    # Loop to traverse the alphabet 
    # in the given string 
    for alphabet in given_str: 
      
        # If alphabet is present 
        # in set vowel 
        if alphabet in vowel: 
            count = count + 1
      
    print("No. of vowels :", count) 
      
# Driver code  
str_to_count_vowels = input("Enter the string you want to count its vowels: ")
  
# Function Call 
vowel_count(str_to_count_vowels) 
