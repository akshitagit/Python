# Python code of Pancake Sort Algorithm

def maxArr(arr, last) :
    
    max = 0

    for i in range(1, last):

        if arr[max] < arr[i] :
            max = i
    
    return max

def swapArr(arr, index) :
    
    index1 = 0

    while index1 < index:
        
        temp = arr[index1]
        arr[index1] = arr[index]
        arr[index] = temp
        index1 = index1 + 1
        index = index - 1

def pancakeSort(arr, size) :
    
    for i in range(size-1, 0, -1):
        
        index = maxArr(arr, i)
        
        if i != index :
            
            swapArr(arr, index)
            swapArr(arr, i)

def main() :

    arr = [54, 85, 52, 25, 98, 75, 25, 11, 68]

    n = len(arr)

    print("Unsorted Array : ", arr)
    
    pancakeSort(arr, n)

    print("Sorted Array : ", arr)


if __name__ == "__main__":
    main()

# Unsorted array : 54 85 52 25 98 75 25 11 68 
# Sorted Array   : 11 25 25 52 54 68 75 85 98 
