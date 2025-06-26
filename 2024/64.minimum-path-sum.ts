/*
 * @lc app=leetcode id=64 lang=typescript
 *
 * [64] Minimum Path Sum
 */

// @lc code=start
function minPathSum(grid: number[][]): number {
  const row = new Array(grid[0].length).fill(Infinity);
  row[row.length - 1] = grid[grid.length - 1][grid[0].length - 1];

  for (let i = grid.length - 1; i >= 0; i--) {
    for (let j = row.length - 1; j >= 0; j--) {
      if (i === grid.length - 1 && j === row.length - 1) {
        continue;
      }
      const nextCol = j + 1 < row.length ? row[j + 1] : Infinity;
      const nextRow = row[j];
      row[j] = grid[i][j] + Math.min(nextRow, nextCol);
    }
  }

  return row[0];
}
// @lc code=end
