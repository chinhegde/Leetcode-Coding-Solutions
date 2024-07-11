# https://leetcode.com/problems/palindromic-substrings/

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = 0
        r = 1

        res = 0 
        

        while l < r:
            sub = s[l:r]

            if sub == sub[::-1]:
                res += 1
            r +=1 
            if r > len(s):
                l += 1
                r = l + 1
            
            if l == len(s):
                break

        return res
        