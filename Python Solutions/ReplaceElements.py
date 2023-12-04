class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rm = -1
        for i in range(len(arr)-1,-1,-1):
            nm = max(rm, arr[i])
            arr[i] = rm
            rm = nm
        return arr