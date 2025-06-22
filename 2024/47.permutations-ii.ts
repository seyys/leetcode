/*
 * @lc app=leetcode id=47 lang=typescript
 *
 * [47] Permutations II
 */

// @lc code=start
function permuteUnique(nums: number[]): number[][] {
      function calc(nums: number[]) {
    const result: number[][] = [];
    if (nums.length === 1) {
      result.push(nums);
    }
    for (let i = 0; i < nums.length; i++) {
      if (i > 0 && nums[i - 1] === nums[i]) {
        continue;
      }
      calc([...nums.slice(0, i), ...nums.slice(i + 1)]).forEach((arr) => {
        result.push([...arr, nums[i]]);
      });
    }
    return result;
  }

  nums.sort();
  return calc(nums);
};
// @lc code=end

