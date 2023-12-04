import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ','')
        chars = re.escape(string.punctuation)
        s = re.sub(r'['+chars+']+', '',s.lower())
        
        if s == s[::-1]: return True
        else: return False