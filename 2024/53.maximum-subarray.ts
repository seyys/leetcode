/*
 * @lc app=leetcode id=53 lang=typescript
 *
 * [53] Maximum Subarray
 */

// @lc code=start
function maxSubArray(nums: number[]): number {
  let maxSum = -Infinity;
  let result = maxSum;
  for (let i = 0; i < nums.length; i++) {
    maxSum = Math.max(maxSum + nums[i], nums[i]);
    result = Math.max(maxSum, result);
  }
  return result;
}
// @lc code=end
