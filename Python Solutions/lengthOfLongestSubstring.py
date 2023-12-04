class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        if len(set(s)) == 1: return 1
        sub = s[0]
        res = len(sub)
        for i in range(1,len(s)):
            if s[i] in sub:
                sub = sub[sub.index(s[i])+1:]
            sub+= s[i]
            if len(sub) > res: res = len(sub)
        return res
        