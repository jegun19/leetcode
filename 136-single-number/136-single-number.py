class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        else:
            temp_dct = {}
            for i in nums:
                if i not in temp_dct:
                    temp_dct[i] = i
                elif i in temp_dct:
                    del temp_dct[i]
                    
            ans = list(temp_dct.keys())[0]
            
            return ans