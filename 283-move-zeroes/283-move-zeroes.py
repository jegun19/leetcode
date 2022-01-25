class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        while i != length-1:
            
            if nums[i] == 0:
                # Determine tail
                j = i + 1
                while j != length and nums[j] == 0:
                    j += 1
                
                if j != length:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                else:
                    break
                
            else:
                i += 1