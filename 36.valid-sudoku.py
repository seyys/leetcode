#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap_i = defaultdict(set)
        hashmap_j = defaultdict(set)
        hashmap_subgrid = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                subgrid = (i // 3, j // 3)
                if val == '.':
                    continue
                if val in hashmap_i[i] or val in hashmap_j[j] or val in hashmap_subgrid[subgrid]:
                        return False
                hashmap_i[i].add(val)
                hashmap_j[j].add(val)
                hashmap_subgrid[subgrid].add(val)
        return True

# @lc code=end

