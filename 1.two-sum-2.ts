/*
 * @lc app=leetcode id=1 lang=typescript
 *
 * [1] Two Sum
 */

// @lc code=start
// @ts-ignore
function twoSum(nums: number[], target: number): number[] {
    const hash = new Object();
    nums.forEach((num, i) => hash[num] = hash[num] ? [...hash[num], i] : [i]);
    for (var i = 0; i < nums.length; i++) {
        const num = nums[i];
        if (hash[target - num] === undefined) continue;
        if (num === (target - num) && hash[num].length === 1) continue;
        if (hash[num].length === 2) return hash[num];
        return [i, hash[target - num][0]];
    }
    return [NaN, NaN]
};
// @lc code=end

