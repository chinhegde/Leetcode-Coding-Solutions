class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1

        for i in range(len(nums)):
            if nums[r]+nums[l] > target:
                r -= 1
            elif nums[r]+nums[l] == target:
                return [l+1,r+1]
            else:
                l += 1

