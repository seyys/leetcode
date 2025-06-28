/*
 * @lc app=leetcode id=89 lang=typescript
 *
 * [89] Gray Code
 */

// @lc code=start
function grayCode(n: number): number[] {
  const result = [0];
  let val = 0;
  for (let i = 1; i < 2 ** n; i++) {
    const lowestSetBit = i & -i
    val ^= lowestSetBit;
    result.push(val);
  }

  return result;
}
// @lc code=end
