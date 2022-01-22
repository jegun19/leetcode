class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lens = len(s)
        lent = len(t)
        
        if lens != lent:
            return False
        else:
            list_s = [char for char in s]
            for char in t:
                if char in list_s:
                    list_s.remove(char)
                else:
                    return False
                
            return True