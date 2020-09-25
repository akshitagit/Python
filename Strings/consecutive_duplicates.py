# Code for removing consecutive duplicates in a string

def remove_duplicates(String): 
	
    # length of a string
	n = len(String)  
 
	if (n < 2) : 
		return
	
	j = 0
	
    # traversing String
	for i in range(n): 
		if (String[j] != String[i]): 
			j += 1
			String[j] = String[i] 
	 
	j += 1
	String = String[:j] 
	return String 
	 

# Driver code
if __name__ =='__main__':
    string=input()
    string=list(string.rstrip())
    print(*remove_duplicates(string),sep="")
