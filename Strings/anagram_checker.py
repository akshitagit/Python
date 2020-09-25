def check(s1, s2): 
      
    # the sorted strings are checked  
    if(sorted(s1)== sorted(s2)): 
        print("The strings are anagrams.")  
    else: 
        print("The strings aren't anagrams.")          
          
# driver code   
s1 = input("enter string 1: ")
s2 = input("enter string 2: ")
check(s1, s2)
