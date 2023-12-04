class Solution(object):
    def maxSubArray(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = maxSum = a[0]
        for num in a[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum