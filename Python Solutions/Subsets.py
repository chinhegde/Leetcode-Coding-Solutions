class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return (list(map(list,(list(chain.from_iterable(combinations(nums, r) for r in range(len(nums)+1)))))))