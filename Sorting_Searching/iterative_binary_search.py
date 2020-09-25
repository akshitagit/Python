# Iterative binary search

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            return mid

    return -1

arr = [2,3,4,5,6,7,8]
print(binary_search(arr, 6))
print(binary_search(arr, 1))
