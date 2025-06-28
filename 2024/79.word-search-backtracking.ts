/*
 * @lc app=leetcode id=79 lang=typescript
 *
 * [79] Word Search
 */

// @lc code=start
function exist(board: string[][], word: string): boolean {
  const DIRECTIONS = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];
  const seen: number[][] = [];

  function dfs(i: number, row: number, col: number) {
    if (i >= word.length) {
      return true;
    }
    if (row < 0 || col < 0 || row >= board.length || col >= board[0].length) {
      return false;
    }
    const ch = word[i];
    if (board[row][col] !== ch) {
      return false;
    }

    if (seen.some((coord) => coord[0] === row && coord[1] === col)) {
      return false;
    }

    const potentialCoords: number[][] = DIRECTIONS.map((dir) => [
      row + dir[0],
      col + dir[1],
    ]);

    seen.push([row, col]);
    if (potentialCoords.some((coords) => dfs(i + 1, coords[0], coords[1]))) {
      return true;
    }
    seen.pop();
    return false;
  }

  for (let row = 0; row < board.length; row++) {
    for (let col = 0; col < board[0].length; col++) {
      if (dfs(0, row, col)) {
        return true;
      }
    }
  }

  return false;
}
// @lc code=end
