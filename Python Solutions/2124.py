# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution:
    def checkString(self, s: str) -> bool:

        try:
            k = s.index('a', s.index('b'))
        except:
            return True

        return False 
        