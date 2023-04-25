/*
 * @lc app=leetcode id=14 lang=typescript
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
function longestCommonPrefix(strs: string[]): string {
    var i = 0;
    var chars: string = "";
    while (true) {
        const nextChar = strs[0][i];
        if (!nextChar) break;
        if (!strs.every(str => str[i] === nextChar)) break;
        i += 1;
        chars += nextChar;
    }
    return chars;
};
// @lc code=end

