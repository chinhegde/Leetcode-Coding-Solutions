import numpy as np

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums
            
            