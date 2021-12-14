class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        c = 0
        length = len(nums)
        while True:
            if (nums[c] == target) or (nums[c] > target):
                return c
            elif (c == length - 1) and (nums[c] < target):
                return length
            else:
                c += 1