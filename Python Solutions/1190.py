# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = list()
        res = list()

        for i in s:
            if i != ")":
                stack.append(i)
            else:
                temp = list()
                while True:
                    k = stack.pop()
                    if k == '(':
                        break
                    temp.append(k)

                stack.extend(temp)
        
        return (''.join(stack))

# 33 ms | Beats 77.83%