class Solution:
    def differenceOfSum(self, n: List[int]) -> int:
        return sum(n) - sum([sum(map(int,str(i))) for i in n])