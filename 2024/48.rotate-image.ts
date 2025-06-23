/*
 * @lc app=leetcode id=48 lang=typescript
 *
 * [48] Rotate Image
 */

// @lc code=start
/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
  const n = matrix.length;
  const offset = Math.floor(n / 2);
  const isOdd = n % 2 === 1;

  for (let row = 0; row < offset + (isOdd ? 1 : 0); row++) {
    for (let col = 0; col < offset; col++) {
      let r = row;
      let c = col;
      let tmp = matrix[r][c];
      for (let i = 0; i < 4; i++) {
        const foo = c
        c = n - 1 - r;
        r = foo;

        const tmp2 = matrix[r][c];
        matrix[r][c] = tmp;
        tmp = tmp2;
      }
    }
  }
}
// @lc code=end
