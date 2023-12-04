class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # hm = dict()
        r = 0
        print(nums)
        nset = set(nums)
        for i in nset:
            if i-1 not in nset:
                l = 1
                while i+l in nset:
                    l+=1
                r = max(r,l)
        return r
