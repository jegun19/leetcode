class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        length = len(position)
        
        if length == 1:
            return 0
        else:
            count_odd = 0
            count_even = 0
            for i in range(0, length):
                if position[i] % 2 != 0:
                    count_odd += 1
                else:
                    count_even += 1
                    
            if count_odd == 0 or count_even == 0:
                return 0
            else:
                return min(count_odd, count_even)