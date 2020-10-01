def countOccOfEachCharacter(s):
    count = [0]*26
    
    for i in s:
        count[ord(i)-97]+=1 
    
    #print count of each chracter 
    for j in s:
        print(str(j)+":"+str(count[ord(j)-97]))
    
try:
    s = input()
    countOccOfEachCharacter(s)
    
except:
    pass
