class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        
        n = len(nums1)

        m = n//2+1

        print(m)
        for i in range(n-m):
            nums1.remove(max(nums1))

        if n%2==0: 
            k1 = max(nums1)
            nums1.remove(max(nums1))
            k2 = max(nums1)

            return (k1+k2)/2
        else: 
            return max(nums1)

        return 1

        