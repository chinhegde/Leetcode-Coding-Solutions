# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        trans = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

        res = list()

        for i in range(len(matrix)):
             mn = min(matrix[i])

             min_ind = matrix[i].index(mn)

             if max(trans[min_ind]) == mn:
                res.append(mn)
                # print(res)

        return res