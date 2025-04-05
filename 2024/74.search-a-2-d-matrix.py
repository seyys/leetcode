#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_row = len(matrix[0])
        len_col = len(matrix)
        lower = 0
        higher = len_row * len_col
        while lower <= higher and lower < (len_row * len_col):
            curr = (higher - lower) // 2 + lower
            val = matrix[curr // len_row][curr % len_row]
            if val > target:
                higher = curr - 1
            elif val < target:
                lower = curr + 1
            elif val == target:
                return True
        return False
# @lc code=end

