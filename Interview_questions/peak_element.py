class Solution(object):
    def findPeakElement(self, nums):
      
        if(len(nums) == 1):
            return 0
        if(len(nums) == 2):
            return nums.index(max(nums))
            
        for i in range(len(nums)):
            
            
            if((i<len(nums)) and (i> 0)):
                if((i == len(nums)-1) and nums[i] > nums[i-1] ):
                    return i
                if(i == 0 and nums[i] > nums[i+1] ):
                    return i
                    
                if(nums[i]> nums[i-1] and nums[i] > nums[i+1]  ):
                    return i
        return 0
               
s = Solution()
print(s.findPeakElement([2 , 4, 6, 8,3]))