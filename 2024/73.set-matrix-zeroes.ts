/*
 * @lc app=leetcode id=73 lang=typescript
 *
 * [73] Set Matrix Zeroes
 */

// @lc code=start
/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
  for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[0].length; col++) {
      if (matrix[row][col] === 0) {
        for (let r = 0; r < matrix.length; r++) {
          if (matrix[r][col] === 0 || Number.isNaN(matrix[r][col])) {
            continue;
          }
          matrix[r][col] = NaN;
        }
        for (let c = 0; c < matrix[0].length; c++) {
          if (matrix[row][c] === 0 || Number.isNaN(matrix[row][c])) {
            continue;
          }
          matrix[row][c] = NaN;
        }
      }
    }
  }

  for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[0].length; col++) {
      if (Number.isNaN(matrix[row][col])) {
        matrix[row][col] = 0;
      }
    }
  }
}
// @lc code=end
