/*
 * @lc app=leetcode id=26 lang=typescript
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
function removeDuplicates(nums: number[]): number {
    const maxValidVal = 100;
    let writeCursor = 0;
    for (let i = 1; i < nums.length; i++){
        if (nums[i] > nums[writeCursor]) {
            nums[++writeCursor] = nums[i];
        }
        if (nums[i] > maxValidVal) break;
    }
    return writeCursor + 1;
};
// @lc code=end

