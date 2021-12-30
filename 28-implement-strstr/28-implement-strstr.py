class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif needle not in haystack:
            return -1
        else:
            if len(needle) == 1:
                for i, char in enumerate(haystack):
                    if char == needle:
                        return i
            else:
                # Check the first and last character from needle
                f_needle = needle[0]
                l_needle = needle[-1]
                
                for i, char in enumerate(haystack):
                    if char == f_needle:
                        if haystack[i + len(needle)-1] == l_needle:

                            found = True
                            for j, remaining in enumerate(needle[1:]):
                                if (i+(j+1)) >= len(haystack):
                                    break
                                elif haystack[i+(j+1)] != remaining:
                                    found = False
                                    break
                            if found:
                                print('yes')
                                return i
                            
                
                if not found:
                    return -1