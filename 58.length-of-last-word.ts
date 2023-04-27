/*
 * @lc app=leetcode id=58 lang=typescript
 *
 * [58] Length of Last Word
 */

// @lc code=start
function lengthOfLastWord(s: string): number {
    let idx = s.length - 1;
    while (s[idx] === ' ') idx--;
    const endOfWord = idx;
    while (idx >= 0 && s[idx] !== ' ') idx--;
    return endOfWord - idx;
};
// @lc code=end

