class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        space = False
        temp = ""
       
        for i in s:
            if i != " ":
                if space == True:
                    space = False
                
                temp += i
            elif i == " " and space == False:
                current_len = len(temp)
                temp = ""
                space = True
                
            elif i == " " and space == True:
                pass
            
        # Final check
        if temp != "":
            current_len = len(temp)
        
        
        return current_len