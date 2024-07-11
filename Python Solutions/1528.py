# https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        ip = list(zip(indices, list(s)))
        ip.sort()

        res = ''.join([j for i,j in ip])
        
        return res