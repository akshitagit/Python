## Kadane's Algorithm O(n)

def checking_max_subarray_sum(arr):
    current_max=arr[0]
    max_so_far=arr[0]
    for i in range(1,len(arr)):
        current_max=max(arr[i],current_max+arr[i])
        max_so_far=max(current_max,max_so_far)
    return max_so_far
arr=input("enter array: ").split()  ## write nos with a space in b/w
arr=[int(x) for x in arr]    
print(checking_max_subarray_sum(arr))    
    
