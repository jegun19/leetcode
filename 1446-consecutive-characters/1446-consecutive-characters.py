class Solution:
    def maxPower(self, s: str) -> int:
        length = len(s)
        
        if length == 1:
            return 1
        else:
            current_char = s[0]
            current_len = 1
            max_len = 1
            
            for i in range(1, length):
                if s[i] != current_char:
                    current_char = s[i]
                    
                    if current_len > max_len:
                        max_len = current_len
                        current_len = 1
                    else:
                        current_len = 1
                        
                elif s[i] == current_char:
                    current_len += 1
                    
            if current_len > max_len:
                max_len = current_len
                
            return max_len
            