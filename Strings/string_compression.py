strin = str(input("enter a string: "))
strarr = dict()
strout = str()
for a in strin:
	if a in strarr.keys():
		strarr[a]+=1
	else:
		strarr[a]=1
for b in strarr.keys():
	strout += b+str(strarr[b])
print(strout)
