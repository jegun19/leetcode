class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lens = len(s)
        lent = len(t)
        
        if lens != lent:
            return False
        else:
            list_s = sorted(s)
            list_t = sorted(t)
            
            if list_s == list_t:
                return True
            else:
                return False