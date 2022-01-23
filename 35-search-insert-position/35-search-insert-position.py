class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if target > nums[length-1]:
            return length
        elif target < nums[0]:
            return 0
        else:
            left = 0
            right = length-1
            while left <= right:
                c = int((left+right)/2)
                if nums[c] == target:
                    return c
                elif nums[c] < target:
                    left = c + 1
                elif nums[c] > target:
                    right = c - 1
                    
            return left