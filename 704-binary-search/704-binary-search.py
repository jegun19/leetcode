class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:
            left = 0
            right = length - 1
            
            while left != right:
                c = int((left+right) / 2)
                if nums[c] < target and right != (left + 1):
                    left = c
                elif nums[c] < target and right == (c + 1):
                    if nums[right] == target:
                        return right
                    else:
                        return -1
                elif nums[c] > target:
                    right = c
                elif nums[c] == target:
                    return c
            
            return -1