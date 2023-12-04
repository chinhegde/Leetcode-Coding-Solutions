class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stk = list()
        res = 0
        print(tokens)
        for i in tokens:
            if i == '+':
                stk.append(stk.pop() + stk.pop())
                # print(stk)
            elif i == '*':
                stk.append(stk.pop() * stk.pop())
                # print(stk)
            elif i == '/':
                b = stk.pop()
                t = stk.pop()
                stk.append(int(t/b))
                # print(stk)
            elif i == '-':
                stk.append(-stk.pop() + stk.pop())
                # print(stk)
            else:
                stk.append(int(i))
        return stk[0]
