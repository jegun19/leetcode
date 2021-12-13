class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        length = len(digits)
        answer = list()
        if length == 0:
            return answer
        elif length == 1:
            length_combination = len(dictionary[digits])
            letters = dictionary[digits]
            for i in range(0, length_combination):
                answer.append(letters[i])
                
            return answer
        
        else:
            # Initialization
            last_char = digits[-1]
            
            for i in range(0, len(dictionary[last_char])):
                answer.append(dictionary[last_char][i])
            
            temp_answer = list()
            # Exclude the last digit
            start = length - 2
            for i in range(start, -1, -1):
                current_list = dictionary[digits[i]]
                length_answer = len(answer)
                
                
                for i in range(0, len(current_list)):
                    current_char = current_list[i]
                    
                    for j in range(0, length_answer):
                        temp_answer.append(current_char + answer[j])
                        
                answer = temp_answer.copy()
                temp_answer.clear()
                
            return answer
                        
                    