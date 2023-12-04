import string

class Solution:
    def titleToNumber(self, ct: str) -> int:

        letters = string.ascii_uppercase
        vals = range(1,27)

        hm = dict(zip(letters, vals))

        res = 0

        for c in ct:
            res *= 26
            res += hm[c]

        return res