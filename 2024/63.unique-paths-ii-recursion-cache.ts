/*
 * @lc app=leetcode id=63 lang=typescript
 *
 * [63] Unique Paths II
 */

// @lc code=start
function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
  function dfs(row: number, col: number): number {
    if (`${row},${col}` in cache) {
      return cache[`${row},${col}`];
    }
    if (row >= obstacleGrid.length || col >= obstacleGrid[0].length) {
      return 0;
    }
    if (obstacleGrid[row][col] === 1) {
      return 0;
    }
    if (row === obstacleGrid.length - 1 && col === obstacleGrid[0].length - 1) {
      return 1;
    }
    const result = dfs(row + 1, col) + dfs(row, col + 1);
    cache[`${row},${col}`] = result;
    return result;
  }

  const cache = {};

  return dfs(0, 0);
}
// @lc code=end
