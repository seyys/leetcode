/*
 * @lc app=leetcode id=90 lang=typescript
 *
 * [90] Subsets II
 */

// @lc code=start
function subsetsWithDup(nums: number[]): number[][] {
  const result: number[][] = [];
  const combination: number[] = [];
  nums.sort();

  function dfs(i: number) {
    result.push([...combination]);
    if (i >= nums.length) {
      return;
    }
    for (let idx = i; idx < nums.length; idx++) {
      if (idx > i && nums[idx] === nums[idx - 1]) {
        continue;
      }
      combination.push(nums[idx]);
      dfs(idx + 1);
      combination.pop();
    }
  }

  dfs(0);
  return result;
}
// @lc code=end
