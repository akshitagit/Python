def check(a, b):
    switch = 1
    if len(a) == len(b) and sorted(a) == sorted(b):
        switch = 1
    else:
        switch = 0
    return switch

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("True") if check(str1, str2) == 1 else print("False")
