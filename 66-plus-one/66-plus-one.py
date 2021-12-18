class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        found = False
        if length == 1:
            if digits[0] == 9:
                digits.append(0)
                digits[0] = 1
                
                return digits
            else:
                digits[0] += 1
                
                return digits
            
        else:
            if digits[-1] == 9:
                digits[-1] = 0
                for i in range(length-2, -1, -1):
                    if digits[i] == 9:
                        digits[i] = 0
                    else:
                        found = True
                        digits[i] += 1
                        break
                        
                if not found:
                    digits.insert(0, 1)
                    
                return digits
                    
                
            else:
                digits[-1] += 1
                
                return digits