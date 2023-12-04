class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        from collections import Counter

        dict_s = dict(Counter(s))

        for c in t:
            if c not in dict_s:
                return c
            else:
                dict_s[c] -= 1

        return [k for k, v in dict_s.items() if v<0][0]