class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)

        while l<r:
            m = l + (r-l)//2
            print(m, nums[m])
            if target > nums[m]:
                l = m+1
            else:
                r = m
        return l
