#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        left, right = 0, (num_rows * num_cols) - 1

        while left <= right:
            middle = (right + left) // 2
            row = (middle) // num_cols
            col = (middle) % num_cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = middle - 1
            else:
                left = middle + 1

        return False

# @lc code=end

