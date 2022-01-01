class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        
        if length == 1:
            return 0
        elif length == 2:
            if nums[0] > nums[1]:
                return 0
            elif nums[1] > nums[0]:
                return 1
        else:
            for i in range(0, length):
                if i == 0:
                    if nums[i] > -(2**31)-1 and nums[i] > nums[i+1]:
                        return i    
                
                if i == length-1:
                    if nums[i] > nums[i-1] and nums[i] > -(2**31)-1:
                        return i    
                
                else:
                    if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                        return i
                
            return 0