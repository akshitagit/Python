def decToOc(decimal):
    res = decimal
    if decimal > 7:
        res = int(str(decimal//8) + str(decimal%8))
    print("The octal number of {} is {}".format(decimal,res))
decToOc(int(input("Enter the decimal number : ")))