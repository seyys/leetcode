/*
 * @lc app=leetcode id=1 lang=typescript
 *
 * [1] Two Sum
 */

// @lc code=start
function twoSum(nums: number[], target: number): number[] {
  const hashmap = new Map<number, number>();
  nums.forEach((num, i) => hashmap.set(target - num, i));
  for (let i = 0; i < nums.length; i++) {
    if (hashmap.has(nums[i]) && hashmap.get(nums[i]) !== i) {
      const index = hashmap.get(nums[i]);
      if (!index) {
        throw new Error('There must be a result')
      }
      return [i, index];
    }
  }
  throw new Error('There must be a result');
}
// @lc code=end
