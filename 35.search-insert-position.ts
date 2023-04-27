/*
 * @lc app=leetcode id=35 lang=typescript
 *
 * [35] Search Insert Position
 */

// @lc code=start
function searchInsert(nums: number[], target: number): number {
    let lowIdx = 0;
    let highIdx = nums.length - 1;
    while (true) {
        if (lowIdx === highIdx) {
            return nums[lowIdx] < target ? lowIdx + 1 : lowIdx;
        }
        const midIdx = Math.floor((lowIdx + highIdx) / 2);
        const val = nums[midIdx];
        if (val === target) return midIdx;
        else if (target < val) highIdx = Math.max(midIdx - 1, lowIdx);
        else lowIdx = Math.min(midIdx + 1, highIdx);
    }
};
// @lc code=end

