class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        c = 0
        res = ''
        a = list(a)
        b = list(b)
        
        while a or b or c:
            if a:
                c += int(a.pop())
            if b: 
                c +=int(b.pop())
            res += str(c%2)
            c = c//2
            
        return res[::-1]