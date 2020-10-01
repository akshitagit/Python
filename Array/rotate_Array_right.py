arr = list();     
n=int(input("Enter the count of elements in array: ")) 

print("Enter the numbers :")
for i in range(int(n)):
    num=input()
    arr.append(int(num))
        
r = int(input("Enter the number of times u want to rotate the array "))     
print("Before rotation: ");    
for i in range(0, len(arr)):    
    print(arr[i]),     
arr=list(reversed(arr[-r:]))+arr[:-r] 
print();        
print("After right rotation of array: ");    
for i in range(0, len(arr)):    
    print(arr[i]), 
