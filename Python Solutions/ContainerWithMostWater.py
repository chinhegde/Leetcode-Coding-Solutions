class Solution:
    def maxArea(self, ht: List[int]) -> int:

        mx = 0
        l = 0
        r = len(ht)-1

        while l<r:
            vol = min(ht[l],ht[r])*(r-l)
            mx = max(mx, vol)

            if ht[l] < ht[r]: l += 1
            else: r -= 1

        return mx
