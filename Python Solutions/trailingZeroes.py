class Solution:
    def trailingZeroes(self, n: int) -> int:
        k = 5
        res = 0
        while k <= n:
            res += n // k
            k = k * 5
        return res