# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            left = 1
            right = n
            while left != right:
                c = int((left + right)/2)
                if isBadVersion(c):
                    right = c
                elif not isBadVersion(c):
                    left = c + 1
                    
            return left