from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [k for k,v in dict(Counter(nums)).items() if v == 1][0]