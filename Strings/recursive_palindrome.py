#!/usr/bin/python3
# Sat 1 Oct 2022
# Authored by: Mohammad Javad Nikbakht <javadnikbakht@mail.com>

# Python3 code to check if a string is palindrome or not in recursive way

def check_string_palindrome(given_string: str):
  string = given_string.lower()
  if(len(string) > 2):
    if(string[0] == string[-1]):
      return check_string_palindrome(string[1 : -1])
    else:
      return False
  else: return string[0] == string[-1]

print(check_string_palindrome(input("check word for palindrome: ")))
