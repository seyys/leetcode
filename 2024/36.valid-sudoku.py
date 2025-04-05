#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result_i = defaultdict(set)
        result_j = defaultdict(set)
        result_subgrid = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                subgrid = (i//3, j//3)
                if val in result_i[i] or val in result_j[j] or val in result_subgrid[subgrid]:
                    return False
                result_i[i].add(val)
                result_j[j].add(val)
                result_subgrid[subgrid].add(val)
        return True
# @lc code=end

