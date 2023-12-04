class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stk = list()
        cur = ''

        for i in path+"/":
            # print(cur, stk)
            if i == "/":
                if cur == '..':
                    if stk: stk.pop()
                elif cur != '' and cur != '.':
                    stk.append(cur)
                cur = ''
            else:
                cur += i

        return "/"+"/".join(stk)