
# coding: utf-8

# In[ ]:


arr = list();     
n=input("Enter the number of elements you want in the array: ")    

#print("Enter the array elements one by one:")
for i in range(int(n)):
    print("Enter the",i+1,"element of the array: ",end='')
    arr.append(int(input()))

#Display the original array    
print("Array before rotation is:",arr)   

#rotation of the array by 3 elements to left by slicing
l=arr[0:3]
del arr[0:3]
arr=arr+l
print('Array after rotation is:',arr)

