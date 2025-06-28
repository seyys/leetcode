/*
 * @lc app=leetcode id=80 lang=typescript
 *
 * [80] Remove Duplicates from Sorted Array II
 */

// @lc code=start
function removeDuplicates(nums: number[]): number {
  let left = 2;
  for (let right = 2; right < nums.length; right++) {
    if (nums[right] === nums[left - 2]) {
      continue;
    }
    nums[left++] = nums[right];
  }

  return left;
}
// @lc code=end
