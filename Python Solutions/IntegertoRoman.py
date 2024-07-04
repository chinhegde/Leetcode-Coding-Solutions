# https://leetcode.com/problems/integer-to-roman/description/
# 12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:

        syms = {
            1:"I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        res = list()
        z = 0

        while num:
            rem = num % 10
            num = num//10
            n = rem * (10**z)
            z += 1

            if rem in [4, 9]:
                if rem == 4:
                    sym1 = (10**z)/2
                    sym2 = 10**(z-1)

                    s = syms[sym2] + syms[sym1]
                    res.append(s)

                if rem == 9:
                    sym1 = (10**z)
                    sym2 = 10**(z-1)

                    s = syms[sym2] + syms[sym1]
                    res.append(s)

            else:
                if rem < 4:
                    sym1 = 10**(z-1)
                    s = syms[sym1]*rem

                    res.append(s)
                else:
                    sym1 = (10**z)/2
                    sym2 = 10**(z-1)

                    s = syms[sym1] + syms[sym2]*(rem-5)

                    res.append(s)
            
        return "".join(res[::-1])