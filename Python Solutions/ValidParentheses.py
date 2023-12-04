class Solution:
    def isValid(self, s: str) -> bool:
        d = {'}':'{', ']':'[', ')':'('}
        stk = list()
        
        for i in s:
            if i == '(' or i == '{' or i =='[':
                stk.append(i)
            elif len(stk)!=0 and stk.pop() == d[i]:
                continue
            else: 
                return False
        if len(stk) != 0: return False
        return True