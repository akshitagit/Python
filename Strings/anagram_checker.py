CHARS = 26
t = int(input())
for i in range(t):
    def remAnagram(a, b): 
        count1 = [0]*CHARS 
        count2 = [0]*CHARS 
        i = 0
        while i < len(a): 
            count1[ord(a[i])-ord('a')] += 1
            i += 1
        i =0
        while i < len(b): 
            count2[ord(b[i])-ord('a')] += 1
            i += 1
        result = 0
        for i in range(26): 
            result += abs(count1[i] - count2[i]) 
        return result 
    if __name__ == "__main__": 
        a = str(input())
        b = str(input())
        print(remAnagram(a, b)) 
'''
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
'''
