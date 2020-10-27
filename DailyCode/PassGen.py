import random                #importing random module for randomly select the entities for password
import sys                   #for terminal operations

def gen_pass(giv_choice,length=8):            #function for generating passwords from given details
    upper_chars="ABCDEFGHIJKLMNOPQRSTUVWXYX"
    lower_chars="abcdefghijklmnopqrstuvwxyz"
    numbers="1234567890"
    special_chars="!@#$%&*?"
    generated_pass=""
    if (giv_choice) ==1:
        for i in range(length):
            generated_pass+=random.choice(upper_chars+lower_chars)  #randomly selecting and adding
        return generated_pass
    elif (giv_choice) ==2:
        for i in range(length):
            generated_pass+=random.choice(upper_chars+lower_chars+numbers)
        return generated_pass
    elif giv_choice == 3:
        mixed=upper_chars+lower_chars+numbers+special_chars
        for i in range(length):
            generated_pass+=random.choice(mixed)
        return generated_pass
    else:
        return False
choice=(input('''\nSelect Complexity Of Password:\n
 1) Simple (Alphabets Only)
 2) Intermediate (Alphabets And Numbers)
 3) Advanced (Upper And Lower Alphabets,Numbers)\n'''))
if choice == '':
    print("\nError,You left input blank..")
    sys.exit()
else:
    choice=int(choice)
length=input("\nHow Much Length Do You Need:(Default:8)=")
try:
    if length != '':
        length=int(length)      #converting length to int to check the given input is an integer
    else:
        length = 8
    password=gen_pass(choice,length)
    if password is False:
        print("\nYou entered wrong choice!!")
        sys.exit()
    else:
        print("\n\nThe Generated Password:\t",password)
except ValueError:
    print("Please Enter A Valid Choice:")
    sys.exit()
print("\n\nThank You For Using..Have a good day")
