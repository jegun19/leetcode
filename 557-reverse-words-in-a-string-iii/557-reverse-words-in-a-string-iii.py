class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseString(s):
            s = list(s)
            length = len(s)

            for i in range(0, int(length/2)):
                s[i], s[length-i-1] = s[length-i-1], s[i]
                
            t = ''.join(s)

            return t
        
        lw = s.split(' ')
        lr = list()
        for w in lw:
            lr.append(reverseString(w))
        
        x = ' '.join(lr)
        return x
    
    