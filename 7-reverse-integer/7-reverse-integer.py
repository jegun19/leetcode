import math
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x == 0:
            return 0
        else:
            if x > 0:
                negative = False
            elif x < 0:
                negative = True
                
            x = abs(x)
            rank = int(math.log10(x))
            if rank == 0:
                return x
            else:
                for i in range(0, rank + 1):
                    division = x / (10 ** rank)
                    if (division < 1) and (rank != 0):
                        rank -= 1
                    else:
                        result += int(division) * (10 ** i)
                        x -= int(division) * (10 ** rank)
                        rank -= 1

                if negative:
                    result = result * -1
                    
                low_range = -(2 ** 31) 
                hi_range = (2**31) - 1
                
                if result < low_range or result > hi_range:
                    return 0
                else:
                    return result