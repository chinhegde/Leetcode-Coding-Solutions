class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        row, col = len(mat), len(mat[0])

        top = 0
        bot = row -1

        while top <= bot:
            mid = (top+bot)//2

            if mat[mid][0] > target:
                bot = mid - 1
            elif mat[mid][-1] < target:
                top = mid + 1
            else:
                break

        if not (top<=bot):
            return False

        rn = (top+bot)//2
        l = 0
        r = col - 1

        while l<=r:
            m = (l+r)//2
            if mat[rn][m] > target:
                r = m - 1
            elif mat[rn][m] < target:
                l = m + 1
            else:
                return True
        
        return False