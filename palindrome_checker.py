'''

                            Palindrome checker by python

'''
def palindrome (s):
    r=s[::-1]
    if(r==s):
        print("Yes")
    else:
        print("No")
s = input()
palindrome(s)

