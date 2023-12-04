class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # list(set(range(len(nums))).difference(set(nums)))[0]
        print(set(range(len(nums)+1)))
        print(set(nums))
        return (list(set(range(len(nums)+1)).difference(set(nums)))[0])
