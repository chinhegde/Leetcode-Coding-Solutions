# https://leetcode.com/problems/zigzag-conversion/
# 6. Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s): return s

        res = ['']*numRows
        col = 0
        dr = True # direction 

        for i in s:
            
            res[col] += i
            if col == len(res)-1 or col == 0:
                dr = not dr
            col += -1 if dr else +1

        return ''.join(res)