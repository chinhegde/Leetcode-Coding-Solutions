class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rset = list(zip(list(range(0,9)), board))

        for i, row in rset:
            nums = [x for x in row if x.isdigit()]
            if len(nums) == len(set(nums)):
                continue
            else:
                return False
        
        cset = list(zip(list(range(0,9)), list(map(list, zip(*board)))))

        for i, col in cset:
            nums = [x for x in col if x.isdigit()]
            if len(nums) == len(set(nums)):
                continue
            else:
                return False
        
        gset = dict()

        for row in range(len(board)):
            for val in range(len(board[row])):
                key = (row//3, val//3)
                
                if key in gset: gset[key].append(board[row][val])
                else: gset[key] = [board[row][val]]

        for grid in gset.values():
            print(grid)
            nums = [x for x in grid if x.isdigit()]
            if len(nums) == len(set(nums)):
                continue
            else:
                return False

        return True











