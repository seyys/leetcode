/*
 * @lc app=leetcode id=1 lang=typescript
 *
 * [1] Two Sum
 */

// @lc code=start
// @ts-ignore
function twoSum(nums: number[], target: number): number[] {
    const diffTargetNums = nums.map(num => target - num);
    var idx1 = NaN;
    var idx2 = NaN;
    nums.findIndex((num1, i) => {
        return diffTargetNums.find((num2, j) => {
            if (num1 !== num2) return false;
            if (i === j) return false;
            idx1 = i;
            idx2 = j;
            return true;
        })
    });
    return [idx1, idx2];
};
// @lc code=end

