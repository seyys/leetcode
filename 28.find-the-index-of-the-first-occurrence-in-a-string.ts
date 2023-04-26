/*
 * @lc app=leetcode id=28 lang=typescript
 *
 * [28] Find the Index of the First Occurrence in a String
 */

// @lc code=start
function strStr(haystack: string, needle: string): number {
    for (let i = 0; i < haystack.length; i++) {
        let found = true;
        for (let j = 0; j < needle.length; j++) {
            if (haystack[i+j] !== needle[j]) {
                found = false;
                break;
            }
        }
        if (found) return i;
    }
    return -1;
};
// @lc code=end

