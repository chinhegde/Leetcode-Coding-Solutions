class Solution:
    def finalValueAfterOperations(self, ops: List[str]) -> int:
        
        # x = len([i for i in ops if '+' in i]) - len([i for i in ops if '-' in i])
        # return x

        return sum([-1 if '-' in i else 1 for i in ops])