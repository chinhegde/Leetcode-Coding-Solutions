class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:            
            r = -1*int(str(-x)[::-1])
            
        else:
            r = int(str(x)[::-1])
        
        if -2**31 < r < 2**31 -1:
            return r
        return 0
        