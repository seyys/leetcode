/*
 * @lc app=leetcode id=63 lang=typescript
 *
 * [63] Unique Paths II
 */

// @lc code=start
function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
  const row = new Array(obstacleGrid[0].length).fill(0);
  row[row.length - 1] = 1;

  for (let i = obstacleGrid.length - 1; i >= 0; i--) {
    for (let j = row.length - 1; j >= 0; j--) {
      if (obstacleGrid[i][j] === 1) {
        row[j] = 0;
      } else {
        row[j] = row[j] + (j + 1 < row.length ? row[j + 1] : 0);
      }
    }
  }

  return row[0];
}
// @lc code=end
