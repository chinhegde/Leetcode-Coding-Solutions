class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        ls = 0
        ts = sum(nums)
        
        for i,x in enumerate(nums):
            if ls == ts - ls - x: return i
            ls+=x
        return -1