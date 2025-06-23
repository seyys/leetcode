/*
 * @lc app=leetcode id=54 lang=typescript
 *
 * [54] Spiral Matrix
 */

// @lc code=start
function spiralOrder(matrix: number[][]): number[] {
  const DIRECTIONS = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];

  let rows = matrix[0].length;
  let cols = matrix.length - 1;
  let dir = 0;
  let r = 0;
  let c = -1;

  const result: number[] = [];
  
  while (cols >= 0 && rows >= 0) {
    const [rowIncrement, colIncrement] = DIRECTIONS[dir];
    for (let i = 0; i < (dir % 2 === 0 ? rows : cols); i++) {
      r += rowIncrement;
      c += colIncrement;
      result.push(matrix[r][c]);
    }
    rows -= dir % 2 === 0 ? 1 : 0;
    cols -= dir % 2 === 1 ? 1 : 0;
    dir = (dir + 1) % 4;
  }

  return result;
}
// @lc code=end
