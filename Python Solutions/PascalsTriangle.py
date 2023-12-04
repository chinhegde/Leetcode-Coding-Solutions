class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if n==1: return [[1]]
        if n==2: return [[1],[1,1]]
        
        res = [[1],[1,1]]
        
        for i in range(1,n-1):
            temp = [1]
            for j in range(len(res[i])):
                if j+1 != len(res[i]):
                    temp.append(res[i][j]+res[i][j+1])
            temp.append(1)
            res.append(temp)
        return res