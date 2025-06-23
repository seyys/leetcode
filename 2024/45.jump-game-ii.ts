/*
 * @lc app=leetcode id=45 lang=typescript
 *
 * [45] Jump Game II
 */

// @lc code=start
function jump(nums: number[]): number {
  const result: number[] = new Array(nums.length).fill(Infinity);
  result[0] = 0;
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums[i] + 1 && i + j < result.length; j++) {
      result[i + j] = Math.min(result[i + j], result[i] + 1);
    }
  }
  return result.at(-1) as number;
}
// @lc code=end
