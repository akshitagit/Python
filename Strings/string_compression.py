strin = str(input("enter a string: "))
strarr = dict()
strout = str()
i = -1
while(i<len(strin)-1):
    i+=1
    ch = strin[i]
    count = 0
    for c in range(i,len(strin)):
        if strin[c]!=ch:
            c-=1
            break
        else:
            count+=1
    strout+= ch + str(count)
    i = c
print(strout)
