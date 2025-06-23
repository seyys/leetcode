/*
 * @lc app=leetcode id=45 lang=typescript
 *
 * [45] Jump Game II
 */

// @lc code=start
function jump(nums: number[]): number {
  let left = 0;
  let right = 0;

  let result = 0;

  while (right < nums.length - 1) {
    let farthest = 0;
    for (let i = left; i < right + 1; i++) {
      farthest = Math.max(i + nums[i], farthest);
    }
    left = right + 1;
    right = farthest;
    result++;
  }

  return result;
}
// @lc code=end
