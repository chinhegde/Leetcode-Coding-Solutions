# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        div = [i for i in range(1,n+1)  if i%m == 0]
        non_div = [i for i in range(1, n+1)  if i%m != 0]

        return sum(non_div) - sum(div)
        