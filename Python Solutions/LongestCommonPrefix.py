class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        
        r = 1
        
        k = 0
        while k < len(min(s, key = len)):
            t = s[0][k]
            for i in s:
                if i[k] == t:
                    continue
                else: r = 0
            if r!=1: break
            k+=1
        
        return s[0][:k]