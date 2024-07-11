# https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        res = 0

        for op in logs:

            if op.startswith(".."):
                if res: res -=1
            elif op[0].isalnum():
                res += 1

        return res