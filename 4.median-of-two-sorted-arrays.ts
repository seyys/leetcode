/*
 * @lc app=leetcode id=4 lang=typescript
 *
 * [4] Median of Two Sorted Arrays
 */

// @lc code=start
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    let totalLen = nums1.length + nums2.length;
    let totalLenEven = false;
    if (totalLen === 2) return [...nums1, ...nums2].reduce((prev, val) => prev += val / 2, 0);
    if (totalLen % 2 === 0) {
        // Remove lowest number
        if (nums2[0] === undefined || nums1[0] < nums2[0]) nums1 = nums1.slice(1);
        else nums2 = nums2.slice(1);
        totalLen = totalLen - 1;
        totalLenEven = true;
    }
    let totalIdx = 0;
    let idx1 = 0;
    let idx2 = 0;
    let result: number = 0;
    let lastResult: number = 0;
    let cursor1 = nums1[idx1++];
    let cursor2 = nums2[idx2++];
    while (totalIdx < Math.ceil(totalLen / 2)) {
        lastResult = result;
        if (cursor2 === undefined || cursor1 < cursor2) {
            result = cursor1;
            cursor1 = nums1[idx1++];
        } else {
            result = cursor2;
            cursor2 = nums2[idx2++];
        }
        totalIdx++;
    }
    if (totalLenEven) result = (result + lastResult) / 2;
    return result;
};
// @lc code=end

