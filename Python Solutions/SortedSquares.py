class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [None for _ in nums]
        l, r = 0, len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[l])>abs(nums[r]):
                res[i] = (nums[l]*nums[l])
                l+=1
            else:
                res[i] = (nums[r]*nums[r])
                r-=1
        
        return res
        