
# coding: utf-8

# In[ ]:




arr = list();     
n=input("Enter the number of elements you want in the array: ")    

print("Enter the array elements one by one:")
for i in range(int(n)):
    ele=input()
    arr.append(int(ele))
     
#Display the original array    
print("Array before rotation is: ")   
for i in range(0, len(arr)):    
    print(arr[i])
     
#Rotate the given array by 3 times towards left    
for i in range(0, 3):    
    #Stores the first element of the array    
    first = arr[0]
        
    for j in range(0, len(arr)-1):    
       #Shift element of array by one    
          arr[j] = arr[j+1]
            
    #First element of array will be added to the end    
    arr[len(arr)-1] = first   
     
print()  
     
#Display the array after 3 left rotations   
print("Array after 3 left rotations is: ");    
for i in range(0, len(arr)):    
    print(arr[i])

