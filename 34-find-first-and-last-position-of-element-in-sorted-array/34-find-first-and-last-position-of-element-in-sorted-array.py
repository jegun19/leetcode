class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length == 0:
            return [-1, -1]
        
        else:
            found = False
            pos_start = -1
            pos_end = -1
            for pos, x in enumerate(nums):
                
                
                if x > target and found == False:
                    return [pos_start, pos_end]
                
                elif x > target and found == True:
                    return [pos_start, pos_end]
                
                elif x == target and found == False:
                    found = True
                    pos_start = pos
                    pos_end = pos
                    
                elif x == target and found == True:
                    pos_end = pos
                    
            return [pos_start, pos_end]