from collections import Counter
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = Counter(nums)
        return [k for k in hm if hm[k] > len(nums)//2][0]