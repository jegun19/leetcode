class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        
        if length == 1:
            if nums[0] == 0:
                return 1
            else:
                return 0
        else:
            nums.sort()
            for i in range(0, length):
                if i != nums[i]:
                    return i
            return length