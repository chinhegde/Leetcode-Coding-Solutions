class Solution:
    def maxProfit(self, p: List[int]) -> int:

        lowest = p[0]
        res = 0
        for i in p:
            if i<lowest: lowest = i
            res = max(res, i - lowest)

        return res
