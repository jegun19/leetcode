class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        else:
            if n == 1:
                return True
            else:
                while n != 1:
                    if n % 2 != 0:
                        return False
                    else:
                        n = int(n / 2)
                        
                return True