def merge(arr):
    if len(arr)>1:
        mid =  len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge(L)
        merge(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1

        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1

        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end =" ")
    print()

# driver code to test the above code
x  = int(input("enter number of terms:"))
y = []
for l in range(0,x):
    z=int(input())

    y.append(z)


arr = [12, 11, 13, 5, 6, 7]
print ("Given array is", end ="\n")
printList(y)
merge(y)
print("Sorted array is: ", end ="\n")
printList(y)
