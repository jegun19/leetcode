class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            storage = list()
            possible_ans = list()
            for letter in s:
                if letter not in storage:
                    storage.append(letter)
                else:
                    pos = storage.index(letter)

                    if pos == 0:
                        print(storage)
                        # possibly not break
                        del storage[pos]
                        storage.append(letter)
                        
                    elif pos == len(storage)-1:
                        temp_answer = storage.copy()
                        possible_ans.append(temp_answer)

                        storage.clear()
                        storage.append(letter)
                    else:
                        possible_ans.append(storage)
                        storage = storage[pos+1:]
                        storage.append(letter)


            if storage:
                possible_ans.append(storage)

            length_possible_ans = list()
            for ans in possible_ans:
                length = len(ans)
                length_possible_ans.append(length)
                
            if not length_possible_ans:
                return 0
            else:
                answer = max(length_possible_ans)

                return answer