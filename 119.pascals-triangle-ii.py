#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prevRow = []
        for row in range(rowIndex + 1):
            pascal_row = [1 for x in range(row+1)]
            for cell in range(1, row):
                pascal_row[cell] = prevRow[cell-1] + prevRow[cell]
            prevRow = pascal_row
        return pascal_row
# @lc code=end