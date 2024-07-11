# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len([i for i in nums if i%3 != 0])
        