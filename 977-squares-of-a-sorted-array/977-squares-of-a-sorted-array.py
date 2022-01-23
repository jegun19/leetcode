class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        write_pointer = len(nums)-1
        arr = [0] * len(nums)
        left_val = nums[left] ** 2
        right_val = nums[right] ** 2
        
        while left <= right:
            print(left, right)
            if left_val > right_val:
                arr[write_pointer] = left_val
                left += 1
                left_val = nums[left] ** 2
            else:
                arr[write_pointer] = right_val
                right -= 1
                right_val = nums[right] ** 2
            write_pointer -= 1
            
        return arr