def check(a, b):
    switch = 1
    if len(a) == len(b):
        for letter in range(len(a)):
            if a[letter] != b[letter]:
                switch = 0
    else:
        switch = 0
    return switch

str1 = sorted(input("Enter first string: "))
str2 = sorted(input("Enter second string: "))

print("True") if check(str1, str2) == 1 else print("False")