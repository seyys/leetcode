/*
 * @lc app=leetcode id=55 lang=typescript
 *
 * [55] Jump Game
 */

// @lc code=start
function canJump(nums: number[]): boolean {
  let movement = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    movement = Math.max(movement, nums[i]);
    movement--;
    if (movement < 0) {
      return false;
    }
  }
  return true;
}
// @lc code=end
