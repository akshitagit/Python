

arr = list();     
n=int(input("Enter the number of elements you want in the array: "))    

#print("Enter the array elements one by one:")
for i in range(int(n)):
    print("Enter the",i+1,"element of the array: ",end='')
    arr.append(int(input()))

#Display the original array    
print("Array before rotation is:",arr)   

#rotation of the array by 3 elements to right by slicing
l=arr[n-3:n]
del arr[n-3:n]
l=l+arr
print(l)
