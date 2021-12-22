class Solution:
    def longestPalindrome(self, s: str) -> str:
            length = len(s)
            if length == 1:
                return s
            elif length == 2:
                if s[0] == s[1]:
                    return s
                else:
                    return s[0]
                
            else:
                # Initialization
                longest = s[0]
                same = True
                
                for i in range(0, length):
                    if i == 0 :
                        prev_char = s[i]
                        if s[i+1] == s[i]:
                            longest = s[i:i+2]
                    else:
                        if s[:int(length/2)] == s[int(length/2):]:
                            return s
                        elif s[:int(length/2)] == s[int(length/2):][::-1]:
                            return s
                        
                        if same:
                            if s[i] != prev_char:
                                same = False
                        prev_char = s[i]
                        prv_idx = i-1
                        nxt_idx = i + 1
                        prv = s[prv_idx]
                        if nxt_idx < length:
                            nxt = s[nxt_idx]
                            
                            if nxt == prv:
                                # Use pivot
                                same_prv = False
                                tmp_string = s[prv_idx: nxt_idx +1]
                                if s[i] == nxt and s[i] == prv:
                                    same_prv = True

                                while True:
                                    prv_idx -= 1
                                    nxt_idx += 1
                                    if prv_idx < 0 or nxt_idx == length:
                                        break
                                    else:
                                        if s[prv_idx] == s[nxt_idx]:
                                            tmp_string = s[prv_idx: nxt_idx +1]
                                            if s[prv_idx] != prv:
                                                same_prv = False
                                            
                                        else:
                                            if same_prv:
                                                if s[prv_idx] == prv:
                                                    tmp_string = s[prv_idx] + tmp_string
                                                elif s[nxt_idx] == nxt:
                                                    tmp_string = s[nxt_idx] + tmp_string
                                                    
                                            break

                                if len(tmp_string) > len(longest):
                                    longest = tmp_string

                            elif nxt == s[i]:
                                # Use mirror
                                tmp_string = s[i: nxt_idx+1]

                                # Offset 
                                prv_idx = i
                                while True:
                                    prv_idx -= 1
                                    nxt_idx += 1
                                    if prv_idx < 0 or nxt_idx == length:
                                            break
                                    else:
                                        if s[prv_idx] == s[nxt_idx]:
                                            tmp_string = s[prv_idx: nxt_idx +1]
                                        else:
                                            break

                                if len(tmp_string) > len(longest):
                                    longest = tmp_string
                                    
                if same:
                    return s
                else:
                    return longest