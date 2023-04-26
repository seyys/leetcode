/*
 * @lc app=leetcode id=27 lang=typescript
 *
 * [27] Remove Element
 */

// @lc code=start
function removeElement(nums: number[], val: number): number {
    let writeCursor = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === val) continue;
        nums[writeCursor++] = nums[i];
    }
    return writeCursor;
};
// @lc code=end

