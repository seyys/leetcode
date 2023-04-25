/*
 * @lc app=leetcode id=3 lang=typescript
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
// @ts-ignore
function lengthOfLongestSubstring(s: string): number {
    const chars = new Set();
    let leftIdx = 0;
    let maxSubStrLen = 0;
    for (let rightIdx = 0; rightIdx < s.length; rightIdx++) {
        const char = s[rightIdx];
        if (!chars.has(char)) {
            chars.add(char);
            maxSubStrLen = Math.max(maxSubStrLen, rightIdx - leftIdx + 1);
        } else {
            while (s[leftIdx] !== char) {
                chars.delete(s[leftIdx++]);
            }
            leftIdx += 1;
        }
    }
    return maxSubStrLen;
};
// @lc code=end

