class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            # Sort the array first
            nums.sort()
            
            max_len = 1
            
            curr_num = nums[0]
            curr_len = 1
            
            for i in range(1, len(nums)):
                if nums[i] != curr_num and nums[i] == curr_num + 1:
                    curr_num = nums[i]
                    curr_len += 1
                elif nums[i] != curr_num:
                    if curr_len > max_len:
                        max_len = curr_len
                    
                    curr_num = nums[i]
                    curr_len = 1
                    
            if curr_len > max_len:
                max_len = curr_len
                    
            return max_len