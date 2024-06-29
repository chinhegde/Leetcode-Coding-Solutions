# Leetcode 402. Remove K Digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stk = list()

        for i in range(len(num)):
            while stk and stk[-1] > num[i] and k>0:
                k-=1
                stk.pop()
            stk.append(num[i])
        while k > 0:
            k-=1
            stk.pop()
        
        while stk and stk[0] == '0':
            stk.pop(0)

        return ''.join(stk) if stk else '0'
        