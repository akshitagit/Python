def fact(number):
    if number==1:
        return 1
    else:
        return number*fact(number-1)
        
        
num=int(input("Number"))        
print("Fact of "+num+" is "+fact(num))
