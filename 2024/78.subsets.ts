/*
 * @lc app=leetcode id=78 lang=typescript
 *
 * [78] Subsets
 */

// @lc code=start
function subsets(nums: number[]): number[][] {
  const result: number[][] = [];
  const max = 2 ** nums.length;

  for (let i = 0; i < max; i++) {
    result.push([]);
    for (let idx = 0, bitmask = 1; bitmask <= max; idx += 1, bitmask <<= 1) {
      if (i & bitmask) {
        result.at(-1)?.push(nums[idx]);
      }
    }
  }

  return result;
}
// @lc code=end
