/*
 * @lc app=leetcode id=78 lang=typescript
 *
 * [78] Subsets
 */

// @lc code=start
function subsets(nums: number[]): number[][] {
  const result: number[][] = [];

  function dfs(idx: number, combination: number[]) {
    result.push(combination);
    if (idx >= nums.length) {
      return;
    }
    for (let i = idx; i < nums.length; i++) {
      dfs(i + 1, [...combination, nums[i]]);
    }
  }

  dfs(0, []);
  return result;
}
// @lc code=end
