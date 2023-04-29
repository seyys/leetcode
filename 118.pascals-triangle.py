#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for row in range(numRows):
            pascal_row = [1 for x in range(row+1)]
            for cell in range(1, row):
                pascal_row[cell] = result[row-1][cell-1] + result[row-1][cell]
            result.append(pascal_row)
        return result
# @lc code=end