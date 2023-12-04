import itertools

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        a = [nums[i::n] for i in range(n)]
        return list(itertools.chain(*a))