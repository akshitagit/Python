class Solution(object):
    def singleNonDuplicate(self, nums):

        # if not sorted -> sort the arr(nums)

        
        def search(arr , low , high):
            
            if(low>high):
                return None
            
            if(low == high):
                return arr[high]
            
            mid = int( low +( high-low)/2)
            
            if( mid%2 == 0):
                if(arr[mid] == arr[mid+1]):
                    return search(arr , mid+2 , high) 
                else:
                    return search(arr, low , mid)
            
            else:
                if(arr[mid] == arr[mid-1]):
                    return search(arr , mid+1 , high)
                else:
                    return search(arr , low,  mid-1)
        
        return search(nums, 0 , len(nums)-1)


# Solution based on Binary Search
# nums must be sorted

s= Solution()
p = s.singleNonDuplicate([2 , 4 , 5 ,6, 6,9])
print(p)
