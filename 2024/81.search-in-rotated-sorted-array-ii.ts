/*
 * @lc app=leetcode id=81 lang=typescript
 *
 * [81] Search in Rotated Sorted Array II
 */

// @lc code=start
function search(nums: number[], target: number): boolean {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((right - left) / 2) + left;
    if (
      nums[mid] === target ||
      nums[left] === target ||
      nums[right] === target
    ) {
      return true;
    }
    // mid is on the lower half, and we haven't found the pivot yet
    if (nums[mid] < nums[left]) {
      if (target < nums[mid] || target > nums[left]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
    // mid is on the upper half, and we haven't found the pivot yet
    else if (nums[mid] > nums[right]) {
      if (target > nums[mid] || target < nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    } else if (nums[left] === nums[right]) {
      left++;
    }
    // otherwise treat as monotonically increasing
    else {
      if (target > nums[mid]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }

  return false;
}
// @lc code=end
