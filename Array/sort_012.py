class Solution():
    
    def sort_main_012(self , nums):

        def sort012( a, arr_size): 
            low = 0
            high = arr_size - 1
            mid = 0
            while (mid <= high): 
                if a[mid] == 0: 
                    a[low], a[mid] = a[mid], a[low] 
                    low = low + 1
                    mid = mid + 1
                elif a[mid] == 1: 
                    mid = mid + 1
                else: 
                    a[mid], a[high] = a[high], a[mid] 
                    high = high - 1
            return a 
        
        return sort012(nums , len(nums))
            
 


s = Solution()
res = s.sort_main_012([ 1 , 0 , 0, 1, 2,1  ,0 , 2 ])
print(res)