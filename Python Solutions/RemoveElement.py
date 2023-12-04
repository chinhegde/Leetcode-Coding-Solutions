class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
#         n = len(nums)
        
#         for i in range(n):
#             try:
#                 nums.remove(val)
#             except:
#                 break
#         return len(nums)

        nums[:] = [i for i in nums if i!= val ]